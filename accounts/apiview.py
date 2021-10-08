from django.shortcuts import render,redirect
from .forms import *
from django.views.generic import ListView, CreateView, DetailView, TemplateView, UpdateView
from django.urls import reverse_lazy
from buyer.models import *
# from django.contrib.auth.models import User
from accounts.models import myUser as User
from django.contrib.auth import get_user_model

# import views
from django.views import View

from braces.views import GroupRequiredMixin

# send mail
from shoppie.settings import EMAIL_HOST_USER
from django.core.mail import send_mail

# rest api

from rest_framework import viewsets
from rest_framework import permissions
# from .serializers import UserSerializer,CategorySerializer
# from .serializers import CategorySerializer, OfferSerializer,
from .serializers import *
from buyer.utils import status

#rest api
from rest_framework.response import Response
from django.views.decorators.csrf import csrf_exempt
#status  return 
from rest_framework import status
from django.utils.decorators import method_decorator
from rest_framework.decorators import api_view
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse
import json
from rest_framework import  permissions
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import  permission_classes

from rest_framework_jwt.views import obtain_jwt_token, refresh_jwt_token
from django.contrib.auth import login, authenticate


# imports
from rest_framework import viewsets


@csrf_exempt
@api_view(['POST','GET'])
def validate(request):
    if request.method=="POST":
        # tk=obtaint(request)
        # print(tk)
        print("===p")
        # username=data.get("username", None)
        # password=data.get("password", None)
        # print(request)
        # data=request.data
        username=request.data["username"]
        password=request.data["password"]
        print(username)
        print(password)
        # t=obtain_jwt_token(request._request)
        # print(t)
        
        user = authenticate(username=username, password=password)
        print(user)
        if user is None:
            pass
        else:
            login(request, user)
            # return JsonResponse(t)
            return JsonResponse("logged",safe=False)
    else:
        return render(request,'registration/login.html')

@csrf_exempt
@api_view(['POST'])
def obtaint(request):
    print(request.data)
    username=request.data["username"]
    password=request.data["password"]
    user = authenticate(username=username, password=password)
    print(user)
    if user is None:
        return Response("no user")
    else:
        login(request, user)
        return Response("user")
        # return obtain_jwt_token(request)
        
    # if request.method=="POST":
    #     u=request.data["username"]
    #     print(u)
    #     return JsonResponse(obtain_jwt_token(request))


def tk(request):
    return obtain_jwt_token(request)
# @csrf_exempt
# @api_view(['POST','GET'])
# def validate(request):
#     print("lg")
#     if request.method=="POST":
#         # username=data.get("username", None)
#         # password=data.get("password", None)
#         username=request.POST["username"]
#         password=request.POST["password"]
#         print(username)
#         print(password)

#         t=obtain_jwt_token(request._request)
#         print(t)
#         print("======")


#         user = authenticate(username=username, password=password)
#         print(user)
#         if user is None:
#             pass
#             # raise serializers.ValidationError(
#             #     'A user with this email and password is not found.'
#             # )
#         else:
#             login(request, user)
#             return JsonResponse(t, safe=False)
#             # return {
#             #     'username':user.username,
#             # #    'token': obtain_jwt_token(request)
#             # }
#     else:
#         print("-----")
#         return render(request,'registration/login.html')

@csrf_exempt
@api_view(['POST'])
def signup(request):
    if request.method=="POST":
        dat=request.data
        # name=request.data('name')
        # username=request.data('username')
        # email=request.data('email')
        # password=request.data('password')

        # pw=dat['password']
        # pw=set_password(pw)
        # print(pw)
        
        dat.update({"status":'Disabled'})
        dat.update({"rule":'buyer'})
        dat.update({"contact":123})
        # ruser=User(name=request.data('name'),username=request.data('data'))
        print(dat)
        # dat.save()

        serializer = SignupSerializer(data=dat)
        if serializer.is_valid():
            print("save")
            serializer.save()
        return Response('user in')



# class signupViewSet(viewsets.ModelViewSet):
#     queryset = User.objects.all()
#     # permission_classes = [permissions.IsAuthenticated]
#     serializer_class = SignupSerializer
#     def create(self, request):
#         print("ccc====")
#         dat=request.data
#         print(dat)
#         dat.update({"status":'Disabled',"rule":'buyer'})
#         # dat.update({"rule":'buyer'})
#         # dat.update({"contact":123})
       
#         serializer = SignupSerializer(data=dat)
#         print(serializer)
#         print(serializer)
#         if serializer.is_valid():
#             print("save")
#             serializer.save()
#         return Response(serializer.data)

class signupViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    # permission_classes = [permissions.IsAuthenticated]
    serializer_class = SignupSerializer
    def create(self, request):
        print("ccc====")
        dat=request.data
        print(dat)
        print(dat['username'])
        username=dat['username']
        password=dat['password']
        email=dat['email']
        name=dat['fullname']
        
        user=User.objects.create_user(username=username,password=password,name=name,email=email,status='Disabled',rule='buyer')
        login(request, user)
        # if user:
        return Response("success")

