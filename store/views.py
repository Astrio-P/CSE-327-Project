from django.shortcuts import render
from django.http import JsonResponse
import json
from .models import *

def viewall(request):
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
    context={'products' :products,'categorys' :categorys,'cartItems' :cartItems}
    return render(request, 'store/viewall.html', context)

def store(request):
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
    
    return JsonResponse('Item was added', safe=False)
