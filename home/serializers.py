# from django.contrib.auth.models import User, Group
from .models import Category, Offer, Product
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
    # product_image = Base64ImageField(
    #     max_length=None, use_url=True,
    # )
    class Meta:
        model = Product
        fields = ['id','name','price','description','product_image','stock','category','author']


# class Base64ImageField(serializers.ImageField):
#     def to_internal_value(self, data):
#         from django.core.files.base import ContentFile
#         import base64
#         import six
#         import uuid

#         if isinstance(data, six.string_types):
#             if 'data:' in data and ';base64,' in data:
#                 header, data = data.split(';base64,')
#             try:
#                 decoded_file = base64.b64decode(data)
#             except TypeError:
#                 self.fail('invalid_image')
#             file_name = str(uuid.uuid4())[:12] # 12 characters are more than enough.
#             # Get the file name extension:
#             file_extension = self.get_file_extension(file_name, decoded_file)

#             complete_file_name = "%s.%s" % (file_name, file_extension, )

#             data = ContentFile(decoded_file, name=complete_file_name)

#         return super(Base64ImageField, self).to_internal_value(data)

#     def get_file_extension(self, file_name, decoded_file):
#         import imghdr

#         extension = imghdr.what(file_name, decoded_file)
#         extension = "jpg" if extension == "jpeg" else extension

#         return extension