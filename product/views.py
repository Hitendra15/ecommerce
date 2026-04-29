from django.shortcuts import render
from .models import Product
from django.contrib.auth.decorators import login_required
from django.db.models import Q
# Create your views here.
def index(request):
    query = request.GET.get('q')
    if query:
        products = Product.objects.filter(Q(name__icontains=query) | Q(description__icontains=query)).order_by('id')
    else:    
        products = Product.objects.all().order_by('id')
    return render(request,'product/index.html',{'products':products})

@login_required
def product_detail(request,slug):
    product = Product.objects.get(slug=slug)
    return render(request,'product/detail.html',{'product':product})


