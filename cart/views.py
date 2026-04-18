from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from product.models import Product
from .cart import Cart
from decimal import Decimal
# Create your views here.
def add_to_cart(request):
    cart = Cart(request)
    if request.method == "POST":
        product_id = request.POST.get('product_id')
        quantity = request.POST.get('quantity')
        product = get_object_or_404(Product,id=product_id)
        cart.add(product=product,quantity=quantity)
        cart_count = cart.__len__()
    return JsonResponse({'success':True,'cart_count':cart_count})

def cart_overview(request):
    cart = Cart(request)
    total_price = cart.get_total_price()
    return render(request,'cart/cart-overview.html',{'cart':cart,'grand_total':total_price})

def cart_delete(request):
    cart = Cart(request)
    if request.POST.get('action') == 'POST':
        product_id = request.POST.get('product_id')
        cart.delete(product_id=product_id)
        total_price = cart.get_total_price()
        cart_count = cart.__len__()
        return JsonResponse({'success':True,'message':'Product deleted from cart','total_price':total_price,'cart_count':cart_count,'product':product_id})
    
def cart_update(request):
    cart = Cart(request)
    if request.method == 'POST':
        product_id = request.POST.get('product_id')
        quantity = request.POST.get('quantity')
        cart.update(id=product_id,quantity=quantity)
        cart_count = cart.__len__()
        total_price = cart.get_total_price()
        item = cart.cart.get(str(product_id))
        item_total = Decimal(item['price']) * Decimal(item['quantity'])
        return JsonResponse({'success':True,'message':'Product updated sucessfully','total_price':total_price,'count':cart_count,'item_total':float(item_total),'product_id':product_id})
