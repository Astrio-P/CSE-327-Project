from django.shortcuts import render
from .models import *

def viewall(request):
     category = request.GET.get('category')

     if category == None:
        products = Product.objects.all()
     else:
         products = Product.objects.filter(category__name=category)

         
     categorys = Category.objects.all()
     context={'products' :products,'categorys' :categorys}
     return render(request, 'store/viewall.html', context)

def store(request):
    products = Product.objects.all()
    categorys = Category.objects.all()
    context={'products' :products,'categorys' :categorys}
    return render(request, 'store/store.html', context)

def cart(request):
    context={}
    return render(request, 'store/cart.html', context)
    
def checkout(request):
    context={}
    return render(request, 'store/checkout.html', context)
    

