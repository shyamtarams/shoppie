from django.shortcuts import render,redirect
from home.models import *
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

@login_required(login_url='/accounts/guest')
def buyerHome(request):
    if Product.objects.all():
        cat=Category.objects.all()
        # dress
        dfprod=Product.objects.filter(category="dress")[:5]
        dsprod=Product.objects.filter(category="dress")[5:10]
        
        # sneakers
        sfprod=Product.objects.filter(category="sneakers")[:5]
        ssprod=Product.objects.filter(category="sneakers")[5:10]
        # print(sprod)
        
        pdt={
            'cat':cat,
            'dfprod':dfprod,
            'dsprod':dsprod,
            'sfprod':sfprod,
            'ssprod':ssprod,
        }
        return render(request,'buyer/buyerhome.html',pdt)


def productView(request,id):
    user=request.user
    author=User.objects.get(username=user)
    prod=Product.objects.get(id=id)
    prods=Product.objects.filter(category=prod.category)
    print(prod)

    if Cart.objects.filter(author=author,product=prod):
        cart=Cart.objects.filter(author=author,product=prod)
    else:
        cart=''
    pdt={
        'cart':cart,
        'prod':prod,
        'prods':prods,
    }
    return render(request,'buyer/productview.html',pdt)

def addCart(request,id):

    user=request.user
    author=User.objects.get(username=user)
    product=Product.objects.get(id=id)
    if Cart.objects.filter(author=author,product=product):
        cart=True
    else:
        cart=False
        crt=Cart(product=product,author=author)
        crt.save()
    return redirect('/buyer/productview/%d'%id,cart)

def viewCart(request):
    user=request.user
    author=User.objects.get(username=user)
    if Cart.objects.filter(author=author):
        pcart=Cart.objects.filter(author=author)
    else: 
        pcart=''

    pdt={
            'pcart':pcart,
        }
    return render(request,'buyer/viewcart.html',pdt)

    


