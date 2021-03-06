# from django.contrib.auth.models import User, Group
from .models import Category, Offer
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

