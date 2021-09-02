from django.shortcuts import render

def store(request):
    context={}
    return render(request, 'store/store.html', context)

def cart(request):
    context={}
    return render(request, 'store/cart.html', context)
    
def checkout(request):
    context={}
    return render(request, 'store/checkout.html', context)
    
def registerPage(request):
    context= {}
    return render(request, 'store/register.html', context)

def loginPage(request):
    context= {}
    return render(request, 'store/login.html', context)