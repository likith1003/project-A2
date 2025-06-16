from django.db import models
from django.contrib.auth.models import User
from seller.models import Product
# Create your models here.
class CustomerProfile(models.Model):
    customer_id = models.IntegerField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    pno = models.CharField(max_length=50)
    add = models.TextField()
    gender = models.CharField(max_length=50)
    profile_pic = models.ImageField(upload_to='customer_profiles')


class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='cart_items')
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    