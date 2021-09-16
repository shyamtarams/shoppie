from django.db import models
# from django.contrib.auth.models import User
from accounts.models import myUser
from home.models import Product
from datetime import timedelta
import datetime

# Create your models here.


class Order(models.Model):
    name=models.CharField(max_length=200)
    address=models.TextField()
    phone=models.CharField(max_length=10)
    zip=models.IntegerField()
    date=models.DateTimeField(auto_now_add=True)
    delivary_date=models.DateTimeField(default=datetime.datetime.now() + timedelta(days=10))
    product=models.ForeignKey(Product,on_delete=models.CASCADE)
    buyer=models.ForeignKey(myUser,on_delete=models.CASCADE, related_name="buyer")
    seller=models.ForeignKey(myUser,on_delete=models.CASCADE, related_name="seller")

