from django import urls
from django.urls import path
from seller.views import *

urlpatterns = [
    path('', home, name='seller_home'),
    path('register', seller_register, name='seller_register'),
    path('login', seller_login, name='seller_login'),
    path('logout', seller_logout, name='seller_logout'),
    path('add_product', add_product, name='add_product'),
    path('my_products', my_products, name='my_products'),
    path('search', search, name='seller_search'),
    path('update_item<pk>',update_item, name='update_item')
]
