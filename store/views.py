from django.shortcuts import render , get_object_or_404
from .models import Product, Category

# Create your views here.

def home(request):
    p = Product.objects.filter(available=True)
    c = Category.objects.all()   
    return render(request, 'store/home.html' , {'product' :p , 'category':c} )

def product_detail(request, slug):
   c = get_object_or_404(Product, slug=slug , in_stock=True)
   return render(request, 'store/products/product_detail.html' , {'product':c})

def category (request, slug):
    c = Category.objects.get(slug=slug)
    p = Product.objects.filter(Category=c)
    return render(request, 'store/products/category.html' , {'category':c , 'product':p})



