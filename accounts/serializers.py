from .models import myUser as User
from rest_framework import serializers
from django.contrib.auth import authenticate
from django.contrib.auth.models import update_last_login


class UserSerializer(serializers.Serializer):
    class Meta:
        model = User
        fields=['id','username','password']
    # def validate(self,data):
    #     username=data.get("username", None)
    #     password=data.get("password", None)
    #     user = authenticate(username=username, password=password)
    #     if user is None:
    #         raise serializers.ValidationError(
    #             'A user with this email and password is not found.'
    #         )
    #     else:
    #         login(request, user)
    #         return {
    #             'username':user.username,
    #         }
       
            
class SignupSerializer(serializers.Serializer):
    class Meta:
        model:User
        fields=['id','username','name','email','password','status','rule']
    
    # def create(sef, request):
    #     pass