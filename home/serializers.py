# from django.contrib.auth.models import User, Group
from .models import Category, Offer, Product, Cart
from rest_framework import serializers

# class UserSerializer(serializers.HyperlinkedModelSerializer):
#     class Meta:
#         model = User
#         fields = ['url', 'username', 'email', 'groups']

class CategorySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Category
        fields = ['name', 'description', 'category_image']
        # fields ="__all__"

class OfferSerializer(serializers.HyperlinkedModelSerializer):
     class Meta:
        model = Offer
        fields = ['offer','baner_img']

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['id','name','price','description','product_image','stock','category','author']


class ProductCartSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cart
        fields = ['id','product','author']

class ProductSearchSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['id','name']

class CartSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cart
        fields = ['id','product','author']

