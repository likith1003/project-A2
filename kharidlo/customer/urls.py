from django.urls import path
from customer.views import *

urlpatterns = [
    path('', home, name='home'),
    path('register', register, name='customer_register'),
    path('user_login', user_login, name='user_login'),
    path('user_logout', user_logout, name='user_logout'),
    path('add_to_cart<pk>', add_to_cart, name='add_to_cart'),
    path('cart', cart, name='cart'),
]
