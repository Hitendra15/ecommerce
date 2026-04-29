from django.shortcuts import render, redirect
from .models import Address,Order,OrderItem
from .forms import AddressForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from cart.cart import Cart
from django.http import JsonResponse
# Create your views here.
@login_required
def orders(request):
    try:
        address = Address.objects.get(user=request.user)
    except Address.DoesNotExist:
        address = None
    form = AddressForm(request.POST or None,instance=address)
    if request.method == 'POST':
        if form.is_valid():
            address = form.save(commit=False)
            address.user = request.user
            address.save()
            messages.success(request,'Address added successfully')
    return render(request,'order/add_address.html',{'hide_sidebar':True,'form':form})

@login_required
def checkout(request):
    cart = Cart(request)
    try:
        address = Address.objects.get(user=request.user)
        return render(request,'order/checkout.html',{'hide_sidebar':True,'address':address,'cart':cart})
    except Address.DoesNotExist:
        return render(request,'order/checkout.html',{'hide_sidebar':True,'cart':cart})
    
@login_required
def place_order(request):
    if request.method == 'POST':
        cart = Cart(request)
        total_amount = cart.get_total_price()
        order = Order.objects.create(user=request.user,total_amount=total_amount)
        for item in cart:
            OrderItem.objects.create(order=order,product=item['product'],quantity=item['quantity'])
            messages.success(request,'Your order has been placed successfully')
    return JsonResponse({'success':True})