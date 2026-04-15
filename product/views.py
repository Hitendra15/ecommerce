from django.shortcuts import render
from .models import Product
# Create your views here.
def index(request):
    products = Product.objects.all().order_by('id')
    return render(request,'product/index.html',{'products':products})

def product_detail(request,slug):
    product = Product.objects.get(slug=slug)
    return render(request,'product/detail.html',{'product':product})