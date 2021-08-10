from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Category(models.Model):
    name=models.CharField(max_length=50)
    description=models.TextField()
    category_image=models.ImageField(upload_to='category_img/')
    def __str__(self):
        return '{} '.format(self.name)

class Product(models.Model):
    name=models.CharField(max_length=50)
    description=models.TextField()
    product_image=models.ImageField(upload_to='product_img/')
    date=models.DateTimeField(auto_now_add=True)
    stock=models.IntegerField()
    category=models.CharField(max_length=50)
    author=models.ForeignKey(User,on_delete=models.CASCADE)
    def __str__(self):
        return '{} '.format(self.name)
    
class Cart(models.Model):
    product=models.ForeignKey(Product,on_delete=models.CASCADE)
    author=models.ForeignKey(User,on_delete=models.CASCADE)
    date=models.DateTimeField(auto_now_add=True)

class Buyer(models.Model):
    author=models.ForeignKey(User,on_delete=models.CASCADE)
    product=models.ForeignKey(Product,on_delete=models.CASCADE)
    date=models.DateTimeField(auto_now_add=True)

class Seller(models.Model):
    author=models.ForeignKey(User,on_delete=models.CASCADE)
    product=models.ForeignKey(Product,on_delete=models.CASCADE)
    date=models.DateTimeField(auto_now_add=True)


    
