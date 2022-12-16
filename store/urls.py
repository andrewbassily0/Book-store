from django.urls import path
from store import views


app_name='store'


urlpatterns = [
    path('', views.home , name='home'),
    path('book/<slug:slug>' , views.product_detail , name='detail' ),
    path('search/<slug:slug>' , views.category,  name= 'category'),

    #path('product/', views.index),

]


