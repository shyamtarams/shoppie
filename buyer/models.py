from django.db import models
from django.contrib.auth.models import User
from home.models import Product

# Create your models here.


class Order(models.Model):
    name=models.CharField(max_length=200)
    address=models.TextField()
    phone=models.CharField(max_length=10)
    zip=models.IntegerField()
    date=models.DateTimeField(auto_now_add=True)
    product=models.ForeignKey(Product,on_delete=models.CASCADE)
    buyer=models.ForeignKey(User,on_delete=models.CASCADE, related_name="buyer")
    seller=models.ForeignKey(User,on_delete=models.CASCADE, related_name="seller")

