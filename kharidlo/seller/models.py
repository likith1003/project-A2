from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class SellerProfile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='seller_profile')
    seller_id = models.IntegerField(primary_key=True)
    seller_name = models.CharField(max_length=50, unique=True)
    contact = models.CharField(max_length=50, unique=True)
    add = models.CharField(max_length=50)
    gstno = models.CharField(max_length=50, unique=True)
    seller_photo = models.ImageField(upload_to='seller_photos')
    
    def  __str__(self):
        return self.seller_name

categories = [
    ('Electronics', 'Electronics'),
    ('Clothing', 'Clothing'),
    ('Mens collection', 'Mens collection'),
    ('Womens collection', 'Womens collection'),
    ('Kids collection', 'Kids collection'),
]
brands = [
    ('Zebronics', 'Zebronics'),
    ('Boat', 'Boat'),
    ('Sony', 'Sony'),
    ('Allen Solly', 'Allen Solly'),
    ('H&M', 'H&M'),
    ('Peter England', 'Peter England'),
    ('Denim', 'Denim')
]
class Product(models.Model):
    seller = models.ForeignKey(User, on_delete=models.CASCADE, related_name='products')
    pid = models.IntegerField(primary_key=True)
    pname = models.CharField(max_length=50)
    desc = models.TextField()
    price = models.FloatField()
    category = models.CharField(max_length=50, choices=categories, default='Electronics')
    brand = models.CharField(max_length=50, choices=brands, default='Boat')
    stock = models.IntegerField()
    discount = models.FloatField()
    picture = models.ImageField(upload_to='Product_images', max_length=None)

    def __str__(self):
        return self.pname+self.seller.first_name
    

class Sales(models.Model):
    seller = models.ForeignKey(User,on_delete=models.CASCADE, related_name='my_sales')
    customer = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)