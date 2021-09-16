from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class myUser(AbstractUser):
    name=models.CharField(max_length=100,default=False)
    contact=models.CharField(max_length=50,default=False)
    status=models.CharField(max_length=10,default=False)
    rule=models.CharField(max_length=10,default=False)
