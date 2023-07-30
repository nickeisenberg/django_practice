from django.shortcuts import render

def store(request):
    context = {}
    to_return = render(request, 'store/store.html', context)
    return to_return

def cart(request):
    context = {}
    to_return = render(request, 'store/cart.html', context)
    return to_return

def checkout(request):
    context = {}
    to_return = render(request, 'store/checkout.html', context)
    return to_return
