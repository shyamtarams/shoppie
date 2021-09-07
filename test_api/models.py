from django.db import models

# Create your models here.

class Heros(models.Model):
    name=models.CharField(max_length=50)
    price=models.IntegerField()

    def __str__(self):
         return '{} {}'.format(self.name,self.price)