from django.shortcuts import render
from .models import *

def viewall(request):
     products = Product.objects.all()
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
    
# def store(request):
#     categorys = Category.objects.all()
#     context={'categorys' :categorys}
#     return render(request, 'store/store.html', context)
   
