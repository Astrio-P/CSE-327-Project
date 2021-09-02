from django.shortcuts import render
from django.http import JsonResponse
import json
from .models import *

def viewall(request):
    """
    This method is used to display all the products in viewall page.
    :param request: it's a HttpResponse from user.
    :type request: HttpResponse.
    :return: this method returns viewall page which is a HTML page.
    :rtype: HttpResponse.
    """
    if request.user.is_authenticated:
            customer = request.user.customer
            order, created = Order.objects.get_or_create(customer=customer, complete=False)
            items = order.orderitem_set.all()
            cartItems = order.getCartItems
    else:
            items=[]
            order = {'getCartTotal':0,'getCartItems':0}
            cartItems = order['getCartItems']

    category = request.GET.get('category')

    if category == None:
        products = Product.objects.all()
    else:
         products = Product.objects.filter(category__name=category)

         
    categorys = Category.objects.all()
    context={'products' :products,'categorys' :categorys,'cartItems' :cartItems, 'category':category}
    return render(request, 'store/viewall.html', context)

def store(request):
    """
    This method is used to display all the products,category list, cart information in homepage page.
    :param request: it's a HttpResponse from user.
    :type request: HttpResponse.
    :return: this method returns a store page which is a HTML page.
    :rtype: HttpResponse.
    """
    if request.user.is_authenticated:
            customer = request.user.customer
            order, created = Order.objects.get_or_create(customer=customer, complete=False)
            items = order.orderitem_set.all()
            cartItems = order.getCartItems
    else:
            items=[]
            order = {'getCartTotal':0,'getCartItems':0}
            cartItems = order['getCartItems']

    products = Product.objects.all()
    categorys = Category.objects.all()
    context={'products' :products,'categorys' :categorys,'cartItems' :cartItems}
    return render(request, 'store/store.html', context)

def cart(request):
    """
    This method is used to display products that were added in the shopping cart in cart page.
    :param request: it's a HttpResponse from user.
    :type request: HttpResponse.
    :return: this method returns a cart page which is a HTML page.
    :rtype: HttpResponse.
    """
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        items = order.orderitem_set.all()
        cartItems = order.getCartItems
    else:
        items=[]
        order = {'getCartTotal':0,'getCartItems':0}
        cartItems = order['getCartItems']
    categorys = Category.objects.all()
    context={'items': items, 'order': order, 'cartItems' :cartItems,'categorys' :categorys}
    return render(request, 'store/cart.html', context)
    
def checkout(request):
    """
    This method is used to calculate and display the amount and products that is being purchased in checkout page.
    :param request: it's a HttpResponse from user.
    :type request: HttpResponse.
    :return: this method returns a checkout page which is a HTML page.
    :rtype: HttpResponse.
    """
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        items = order.orderitem_set.all()
        cartItems = order.getCartItems
    else:
        items=[]
        order = {'getCartTotal':0,'getCartItems':0}
        cartItems = order['getCartItems']
    categorys = Category.objects.all()
    context={'items':items, 'order':order,'categorys' :categorys,'cartItems' :cartItems}
    return render(request, 'store/checkout.html', context)
    
def updateItem(request):
    """
    This method is used to add products to the shopping cart.
    :param request: it's a HttpResponse from user.
    :type request: HttpResponse.
    :return: this method adds item to the cart and refreshes the HTML page.
    :rtype: HttpResponse.
    """
    data = json.loads(request.body)
    productId = data ['productId']
    action = data['action']

    print('Action:' ,action)
    print('Product:', productId)

    customer = request.user.customer
    product = Product.objects.get(id=productId)
    order, created = Order.objects.get_or_create(customer=customer, complete=False)
    
    orderItem, created = OrderItem.objects.get_or_create(order=order, product=product)

    if action == 'add':
        orderItem.quantity = (orderItem.quantity + 1)
    elif action == 'remove':
        orderItem.quantity = (orderItem.quantity - 1)
    orderItem.save()

    if orderItem.quantity <= 0:
        orderItem.delete()
    
    if action == 'delete':
        orderItem.delete()
    return JsonResponse('Item was added', safe=False)

def searchBar(request):
    """
    This method is used to display all the products matching with the searh query in search page.
    :param request: it's a HttpResponse from user.
    :type request: HttpResponse.
    :return: this method returns a search page which is a HTML page.
    :rtype: HttpResponse.
    """
    if request.user.is_authenticated:
            customer = request.user.customer
            order, created = Order.objects.get_or_create(customer=customer, complete=False)
            items = order.orderitem_set.all()
            cartItems = order.getCartItems
    else:
            items=[]
            order = {'getCartTotal':0,'getCartItems':0}
            cartItems = order['getCartItems']

    category = request.GET.get('category')

    if category == None:
        products = Product.objects.all()
    else:
         products = Product.objects.filter(category__name=category)

         
    categorys = Category.objects.all()
    if request.method == 'POST':
        query = request.POST['query']
        if query:
            products = Product.objects.filter(name__icontains=query) | Product.objects.filter(price__icontains=query) | Product.objects.filter(category__name__icontains=query)
            count = products.count()
            return render(request, 'store/searchbar.html', {'products':products, 'query':query,'categorys' :categorys,'cartItems' :cartItems,'count':count})
        else:
            print("No information to show")
            return render(request, 'store/searchbar.html', {})    