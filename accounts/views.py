from django.shortcuts import render,HttpResponse
from django.contrib.auth.decorators import login_required
from random import randint
from django.contrib.auth.models import User

from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
#import form
from .forms import SignUpForm,SellerSignUpForm
# Create your views here.
from shoppie.settings import EMAIL_HOST_USER
from django.core.mail import send_mail
# import os

# guest home 
from home.models import *

# group assign
from django.contrib.auth.models import Group
from django.contrib.auth import get_user_model

#redirect
from django.http import HttpResponseRedirect

#serializer

from .serializers import UserSerializer
from .models import myUser as User
from rest_framework import viewsets

from rest_framework.decorators import api_view
from django.views.decorators.csrf import csrf_exempt




# @login_required()
@login_required(login_url='/accounts/login/')
def dashboard(request):
    print(request.user)
    # request.session['log_id']=request.user
    return render(request,'accounts/profile.html')
    
@login_required(login_url='/accounts/login/')
def test(request):
    print(request.user)
    return render(request,'test.html')

def signup(request):
    print(request.user,"user=======")
    User = get_user_model()
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        # print(form)
        if form.is_valid():
            # rule = form.cleaned_data.get('rule')
            # status = form.cleaned_data.get('status')
            # password = form.cleaned_data.get('password1')
            # print(rule,status,password)
            user=form.save()
            # user.set_password(user.password)
            # user.save()

            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password')
            # user = authenticate(username=username, password=raw_password)
            login(request, user)

            print(request.user)

            user=User.objects.get(username=username)
            my_group = Group.objects.get(name='buyer')
            my_group.user_set.add(user)

            otp=randint(1000,9999)
            print(otp)
            request.session['tp']=otp

            # subject = 'Welcome'
            # message = 'Warm regards, Your otp for shoppie is %d'%otp
            # recepient = form.cleaned_data.get('email')

            # send_mail(subject,message, EMAIL_HOST_USER, [recepient], fail_silently = False)
            
            return redirect('/accounts/verify')
    else:
        form = SignUpForm()
    return render(request, 'signup.html', {'form': form})


def guest(request):
    # user_status=status(request)
    # print(user_status)
    offer=Offer.objects.all()
    if request.method=="POST" and search in request.POST:
        s=request.POST["search"]
        print(s)
        sprod=Product.objects.filter(name__icontains=s)
        print(sprod)
        prod={
            'sprod':sprod,
        }
        return render(request,"buyer/product_search.html",prod)
    # if user_status=="dis":
    #     return redirect("/accounts/status")
    else:
        if Product.objects.all():
            cat=Category.objects.all()
            prod=Product.objects.all()
            cate=Category.objects.none()
            for c in prod:
                cate = cate | Category.objects.filter(name = c.category)
            minp=Product.objects.none()
           
            fprod=Product.objects.none()
            for c in cat:
                prod=Product.objects.filter(category=c.name)[:5]
                for p in prod:
                    fprod=fprod | Product.objects.filter(name=p.name)

            offer=Offer.objects.all()
            print(offer)
            
            pdt={
                'offer':offer,
                'cat':cat,
                'cate':cate,
                'prod':fprod,
                'minp':minp,
            }
            return render(request,'guest_home.html',pdt)
        else:
            cat=Category.objects.all()
            offer=Offer.objects.all()
            pdt={
                'offer':offer,
                'cat':cat,
            }
            return render(request,'guest_home.html',pdt)


def sellersignup(request):
    User = get_user_model()
    if request.method == 'POST':
        form = SellerSignUpForm(request.POST)
        print(form)
        if form.is_valid():
            # rule = form.cleaned_data.get('rule')
            # status = form.cleaned_data.get('status')
            # password = form.cleaned_data.get('password1')
            # print(rule,status,password)
            user=form.save()

            username = form.cleaned_data.get('username')
            # raw_password = form.cleaned_data.get('password1')
            # user = authenticate(username=username, password=raw_password)
            login(request, user)

            otp=randint(1000,9999)
            print(otp)
            request.session['tp']=otp

            user=User.objects.get(username=username)
            my_group = Group.objects.get(name='sellers') 
            my_group.user_set.add(user)

            return redirect('/accounts/verify')
    else:
        form = SellerSignUpForm()
    return render(request, 'sellersignup.html', {'form': form})

def verify(request):
    print(request.user)
    User = get_user_model()
    if request.method=="POST":
        ot=int(request.POST["otp"])
        tp=int(request.session['tp'])
        print(ot)
        print(tp)
        if tp == ot :
            user_status=User.objects.get(username=request.user)
            if user_status.rule == "buyer":
                user_status.status='Enabled'
                print(user_status)
                user_status.save()
                # del request.session['tp']
                return redirect('/buyer/productlist')
            else:
                # del request.session['tp']
                return redirect('/sellerhome')
        else:
            return redirect('/accounts/verify')
    else:
        return render(request,"verify.html")

def check(request):
    print(request.user,"check")
    User = get_user_model()
    user_rule=User.objects.get(username=request.user)
    # if user_rule.rule == "buyer":
    #     return redirect("/buyer/productlist")
    # else:
    #     return redirect("/sellerhome")
    usergroup = None
    if request.user.is_authenticated:
        usergroup = request.user.groups.values_list('name', flat=True).first()
    if usergroup == "sellers":
        return HttpResponseRedirect("/sellerhome")
    elif usergroup == "buyer":
        return HttpResponseRedirect("/buyer/productlist")
    else:
        return HttpResponseRedirect("/admin/")

def sellerCompanyRegister(request):
    if request.method == "POST":
        email=request.method["email"]
        bank=request.method["bank"]
        address=request.method["address"]
        state=request.method["state"]
        city=request.method["city"]
        zip=request.method["zip"]

    else:
        return render(request,"companyRegister.html")

    
# class UserViewSet(viewsets.ModelViewSet):
#     queryset = User.objects.all()
#     serializer_class = UserSerializer
#     def list(self, request):
#         print("")


@csrf_exempt
@api_view(['POST',])
def validate(request):
    if request.method=="POST":
        # username=data.get("username", None)
        # password=data.get("password", None)
        username=request.POST["username"]
        password=request.POST["password"]

        user = authenticate(username=username, password=password)
        if user is None:
            raise serializers.ValidationError(
                'A user with this email and password is not found.'
            )
        else:
            login(request, user)
            return {
                'username':user.username,
            }
    else:
        pass