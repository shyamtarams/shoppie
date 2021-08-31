from django.shortcuts import render,redirect
from home.models import *
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from .utils import *
from django.db.models import Min
from .models import *

@login_required(login_url='/accounts/guest')
def buyerHome(request):
    user_status=status(request)
    print(user_status)
    offer=Offer.objects.all()
    if user_status=="dis":
        return redirect("/accounts/status")
    else:
        if Product.objects.all():
            cat=Category.objects.all()
            prod=Product.objects.all()
            
            # minp=Product.objects.filter().values('price').annotate(Min('price')).order_by('category')
            minp=Product.objects.none()
            # for c in cat:
            #     minp=minp | Product.objects.filter(category=c).values('price','category').annotate(Min('price')).order_by('category')[:1]
                # print(minp)
            # mprod=Product.objects.none()
            # for c in cat:
            #     prod=Product.objects.filter(category=c.name)
            #     for p in prod:
            #         print(Min(p.price))
                    #  mpord= mprod | 
                    

            # print(minp)
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
                'prod':fprod,
                'minp':minp,
        
                # 'dfprod':dfprod,
                # 'dsprod':dsprod,
                # 'sfprod':sfprod,
                # 'ssprod':ssprod,
            }
            return render(request,'buyer/buyerhome.html',pdt)
        else:
            cat=Category.objects.all()
            offer=Offer.objects.all()
            pdt={
                'offer':offer,
                'cat':cat,
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

def allproducts(request,name):
    prod=Product.objects.filter(category=name)
    
    pdt={
            'prod':prod,
        }
    return render(request,"buyer/allproducts.html",pdt)

def orderproduct(request,id):
    user=request.user
    author=User.objects.get(username=user)
    prod=Product.objects.get(id=id)
    prods=Product.objects.filter(category=prod.category)

    if Cart.objects.filter(author=author,product=prod):
        cart=Cart.objects.filter(author=author,product=prod)
    else:
        cart=''

    if request.method=="POST":
        name=request.POST["name"]
        address=request.POST["address"]
        phone=request.POST["phone"]
        zip=request.POST["zip"]
        print(name)
        seller=prod.author
        print(seller)
        order=Order(name=name,address=address,phone=phone,zip=zip,product=prod,buyer=author,seller=prod.author)
        order.save()
    
    pdt={
        'cart':cart,
        'prod':prod,
        'prods':prods,
    }
    return render(request,"buyer/placeorder.html",pdt)
    

    


