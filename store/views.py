from django.shortcuts import render , HttpResponse 
from .models import Product, Category

# Create your views here.

def category(request):
   
    return ( )

def index(request):
    p = Product.objects.all()
    c = Category.objects.all()   
    return render(request, 'store/home.html' , {'product' :p , 'category':c} )



