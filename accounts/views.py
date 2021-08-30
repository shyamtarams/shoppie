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
    # print(os.getenv('EMAIL_HOST_USER'))
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()

            otp=randint(1000,9999)
            print(otp)
            request.session['tp']=otp

            subject = 'Welcome'
            message = 'http://localhost:8000/buyer/productlist'
            recepient = form.cleaned_data.get('email')

            
            # send_mail(subject,message, EMAIL_HOST_USER, [recepient], fail_silently = False)
            
            # username = form.cleaned_data.get('username')
            # raw_password = form.cleaned_data.get('password1')
            # user = authenticate(username=username, password=raw_password)
            # login(request, user)
            return redirect('/accounts/verify')
    else:
        form = SignUpForm()
    return render(request, 'signup.html', {'form': form})

def guest(request):
    return render(request,"guest_home.html")

def sellersignup(request):
    if request.method == 'POST':
        form = SellerSignUpForm(request.POST)
        if form.is_valid():
            form.save()

            # otp=randint(1000,9999)
            # print(otp)
            # request.session['tp']=otp


            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('/accounts/dashboard')
    else:
        form = SellerSignUpForm()
    return render(request, 'sellersignup.html', {'form': form})

def verify(request):
    if request.method=="POST":
        ot=int(request.POST["otp"])
        tp=int(request.session['tp'])
        print(ot)
        print(tp)
        if tp == ot :
            status=User.objects.get(username=request.user)
            status.last_name=''
            status.save()
            return redirect('/buyer/productlist')
        else:
            return redirect('/accounts/verify')
    else:
        return render(request,"verify.html")




        


    

