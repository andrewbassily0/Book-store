from django.db import models
from django.contrib.auth.models import User 

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=100 , db_index=True)
    slug = models.SlugField(max_length=100, unique=True)

    class Meta:
        verbose_name_plural = 'categories'

    def __str__(self):
        return self.name

class Product(models.Model):
    title = models.CharField(max_length=100, db_index=True)
    price= models.DecimalField(max_digits=4, decimal_places=2)
    description = models.TextField(blank=True)
    image= models.ImageField(upload_to='media/')
    created_by= models.ForeignKey(User, related_name='product_creator' , on_delete=models.CASCADE )
    Category = models.ForeignKey(Category , related_name='product', on_delete=models.CASCADE) 
    slug = models.SlugField(max_length=100)
    in_stock = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = 'Product'
        ordering = ('-created', ) 

    def __str__(self):
        return self.title
