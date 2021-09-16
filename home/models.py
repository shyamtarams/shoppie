from django.db import models
from django.contrib.auth.models import User
from accounts.models import myUser

# # Create your models here.


class Category(models.Model):
    name=models.CharField(max_length=50)
    description=models.TextField()
    category_image=models.ImageField(upload_to='category_img/')
    def __str__(self):
        return '{} '.format(self.name)

class Product(models.Model):
    name=models.CharField(max_length=50)
    price=models.IntegerField()
    description=models.TextField()
    product_image=models.ImageField(upload_to='product_img/')
    date=models.DateTimeField(auto_now_add=True)
    stock=models.IntegerField()
    category=models.CharField(max_length=50)
    author=models.ForeignKey(myUser,on_delete=models.CASCADE)
    
    def __str__(self):
        return '{} {} {} {} {} {} '.format(self.name,self.category,self.description,self.product_image,self.stock,self.price)
    
    def delete(self, *args, **kwargs):
        self.product_image.delete()
        super().delete(*args, **kwargs)
    
class Cart(models.Model):
    product=models.ForeignKey(Product,on_delete=models.CASCADE)
    author=models.ForeignKey(myUser,on_delete=models.CASCADE)
    date=models.DateTimeField(auto_now_add=True)

# # class Buyer(models.Model):
# #     author=models.ForeignKey(myUser,on_delete=models.CASCADE)
# #     product=models.ForeignKey(Product,on_delete=models.CASCADE)
# #     date=models.DateTimeField(auto_now_add=True)

# # class Seller(models.Model):
# #     author=models.ForeignKey(myUser,on_delete=models.CASCADE)
# #     product=models.ForeignKey(Product,on_delete=models.CASCADE)
# #     date=models.DateTimeField(auto_now_add=True)

class Offer(models.Model):
    offer=models.CharField(max_length=50)
    baner_img=models.ImageField(upload_to='offer_img/')
    date=models.DateTimeField(auto_now_add=True)

    def delete(self, *args, **kwargs):
        self.baner_img.delete()
        super().delete(*args, **kwargs)
    
