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







# class UserViewSet(viewsets.ModelViewSet):
#     queryset = User.objects.all().order_by('-date_joined')
#     serializer_class = UserSerializer
#     permission_classes = [permissions.IsAuthenticated]

class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all().order_by('name')
    print(queryset)
    serializer_class = CategorySerializer

class OfferViewSet(viewsets.ModelViewSet):
    queryset = Offer.objects.all()
    serializer_class = OfferSerializer

#create product api
class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    # permission_classes = [permissions.IsAuthenticated]
    serializer_class = ProductSerializer
    #list product
    def list(self, request):
        print("--------")
        serializer_class = ProductSerializer(self.queryset, many=True)
        print(serializer_class)
        return Response(serializer_class.data)
    #create product
    # @method_decorator(csrf_exempt)
    def create(self, request):
        print("post")
        data=request.data
        print(data)
        print(data["name"])
        # print(data["product_image"])
        data.update({"author":'21'})
        print(data)
        serializer = ProductSerializer(data=request.data)
        print(serializer)
        if serializer.is_valid():
            print("save")
            serializer.save()
        return Response(serializer.data)
    #update product
    def update(self, request, pk):
        product = Product.objects.get(pk=pk)
        print(product.product_image)
        print(request.data)
        serializer = ProductSerializer(product, data=request.data)
        # print(serializer)
        if serializer.is_valid():
            print("save")
            serializer.save()
        return Response(serializer.data)
    #delete product
    def destroy(self, request,pk):
        product = Product.objects.get(pk=pk)
        product.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


@csrf_exempt
@api_view(['POST','GET'])
# @permission_classes((IsAuthenticated,))
def postpro(request):
    print("function")
    # if request.method=="POST" and 'uid' in request.POST:
    #     print(request.data)
    if request.method == 'POST':
        name=request.data["name"]
        description=request.data["description"]
        category=request.data["category"]
        price=request.data["price"]
        stock=request.data["stock"]
        stock=request.data["stock"]
        prodimg=request.data["image"]
        id=request.data["id"]
        user=myUser.objects.get(id=id)
        prod=Product(name=name,description=description,category=category,price=price,stock=stock,product_image=prodimg,author=user)
        prod.save()
        return JsonResponse('data in', safe=False)
    
    if request.method=="GET":
        user= Product.objects.all()
        u_serializers = ProductSerializer(user, many='True' )
        return JsonResponse(u_serializers.data, safe=False)

    
@csrf_exempt
@api_view(['POST',])
def listprod(request):
    id=request.data['uid']
    user= Product.objects.filter(author=id)
    u_serializers = ProductSerializer(user, many='True' )
    return JsonResponse(u_serializers.data, safe=False)


@csrf_exempt
@api_view(['PUT'])
def uppro(request):
    print(request.method)
    if request.method=="PUT":
        print(request.data["id"])
        prod=Product.objects.get(id=request.data["id"])
        print(request.data["name"])
        prod.name=request.data["name"]
        prod.price=request.data["price"]
        prod.stock=request.data["stock"]
        prod.description=request.data["description"]
        if request.data["category"]:
            prod.category=request.data["category"]
            # prod.category="gadgets"
        else:
            pass
        if request.data["product_image"]== "undefined":
            print(prod.product_image,"pro image un")
            prod.product_image=prod.product_image
        else:
            print(request.data["product_image"],"pro image ch")
            prod.product_image=request.data["product_image"]
           
        print(prod)
        prod.save()
        return JsonResponse("updated",safe=False)

@csrf_exempt
@api_view(['DELETE'])
def dlpro(request):
    print(request.data["pid"])
    if request.method=="DELETE":
        # print(request.data["id"])
        print(request.delete)
        prod=Product.objects.get(id=id)
        prod.delete()
        return Response(status=status.HTTP_204_NO_CONTENT,safe=False)

class ProductCartViewSet(viewsets.ModelViewSet):
    # queryset = Cart.objects.all()
    # permission_classes = [permissions.IsAuthenticated]
    serializer_class = ProductCartSerializer
    def get(request, self):
        serializer_class = ProductCartSerializer(self.queryset, many=True)
        print(serializer_class)
        return Response(serializer_class.data)
    def get_queryset(self):
        return Cart.objects.filter(author=self.request.user)
    def post(self, request):
        data=request.data
        # data.update({"author":'11'})
        print(data)
        serializer = ProductSerializer(data=request.data)
        print(serializer)
        if serializer.is_valid():
            print("save")
            serializer.save()
        return Response(serializer.data)


@csrf_exempt
@api_view(['POST'])
# @permission_classes((IsAuthenticated,))
def create(request):
    if request.method =="POST":
        print(request.data)
        # print()
       


@csrf_exempt
@api_view(['POST'])
def check(request):
    if request.method == "POST":
        id=request.data
        role=User.objects.get(id=id)
        rl=role.rule
        print(rl)
        return Response(rl)

@csrf_exempt
@api_view(['POST'])
def search(request):
    s=request.data['sr']
    print(s)
    res=Product.objects.filter(name__icontains=s)
    # return Response(res)
    u_serializers = ProductSearchSerializer(res, many='True' )
    return JsonResponse(u_serializers.data, safe=False)

@csrf_exempt
@api_view(['GET'])
def listproduct(request):
    res=Product.objects.all()
    print(res,"==========")
    serializer_class = ProductSerializer(res, many=True)
    print(serializer_class)
    return JsonResponse(serializer_class.data, safe=False)



    # if request.method == "POST":
    #     s=request.data['sr']
    #     res=Product.objects.filter(name__icontains=s)
    #     print(s)
    #     print(res)
    #     return Response(res)


# class ProductSearchViewSet(viewsets.ModelViewSet):
#     def post(request, self):
#         data=request.data
#         print(data)
#         serializer = ProductSearchSerializer(data=request.data)
#         print(serializer)
#         return Response(serializer.data)

#     def get_queryset(self):
#         s=request.data['sr']
#         print(s)
#         return Product.objects.filter(name__icontains=s)


@csrf_exempt
@api_view(['POST'])
def proddetails(request):
    id=request.data['pid']
    user= Product.objects.get(id=id)
    print(user,"===========")
    u_serializers = ProductSerializer(user )
    return JsonResponse(u_serializers.data, safe=False)

@csrf_exempt
@api_view(['POST'])
def cateprod(request):
    cate=request.data['cate']
    prod= Product.objects.filter(category=cate)
    print(prod,"--------------------")
    u_serializers = ProductSerializer(prod, many='True')
    return JsonResponse(u_serializers.data, safe=False)

@csrf_exempt
@api_view(['POST','GET'])
def cartprod(request):
    if request.method =="POST":
        print(request.data)
        u=request.data
        print(u)
        ctid=request.data['u']
        pid=ctid['pid']
        uid=ctid['uid']

        prod= Product.objects.get(id=pid)
        user=User.objects.get(id=uid)
        cart=Cart(author=user,product=prod)
        cart.save()
        print(cart)
        return Response("product added to cart")

@csrf_exempt
@api_view(['POST'])
def viewcart(request):
    uid=request.data['uid']
    print(uid)
    user=User.objects.get(id=uid)
    cart=Cart.objects.filter(author=uid)
    print(cart)
    # prod=Product.objects.filter(id=cart.product)//cart
    # for i in cart:
    #     prod=Product.objects.filter(id_in=i.product)//cart
    # u_serializers = CartSerializer(cart, many='True')
    prod=Product.objects.filter(cart__author=uid)
    u_serializers = ProductSerializer(prod, many='True')
    return JsonResponse(u_serializers.data, safe=False)

@csrf_exempt
@api_view(['POST'])
def checkcart(request):
    pid=request.data['pid']
    print(pid,"c====")
    # c=Cart.objects.get(product=pid)
    # print(c,"==c")
    if Cart.objects.filter(product=pid):
        print("True ")
        return Response('cart')
    else:
        print("False c")
        return Response('no')
    
     
    
        

   
