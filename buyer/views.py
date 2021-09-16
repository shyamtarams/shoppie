from django.shortcuts import render,redirect
from home.models import *
# from django.contrib.auth.models import User
from accounts.models import myUser as User
from django.contrib.auth.decorators import login_required
from .utils import *
from django.db.models import Min
from .models import *
from .forms import ProductSearchForm

# send mail
from shoppie.settings import EMAIL_HOST_USER
from django.core.mail import send_mail

#import views
from django.views import  View
from braces.views import GroupRequiredMixin
# from rest_framework.decorators import api_view

# buyer home class
# @login_required(login_url='/accounts/guest')
class buyerhome(GroupRequiredMixin, View):
    group_required = u"buyer"
    def get(self, request):
        user_status=status(request)
        if user_status=="Disabled":
            return redirect("/accounts/verify")
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
                return render(request,'buyer/buyerhome.html',pdt)
            else:
                cat=Category.objects.all()
                offer=Offer.objects.all()
                pdt={
                    'offer':offer,
                    'cat':cat,
                }
                return render(request,'buyer/buyerhome.html',pdt)
                
    def post(self,request):
        if request.method =="POST":
            form = ProductSearchForm(request.POST)
            if form.is_valid():
                psearch=form.cleaned_data['search']
                sprod=Product.objects.filter(name__icontains=psearch)
                pdt={
                    'sprod':sprod,
                }
                return render(request,"buyer/product_search.html",pdt)
        else:
            return redirect("buyer/productlist")
            

class productview(GroupRequiredMixin, View):
    group_required = u"buyer"

    def get(self, request, *args, **kwargs):
        id=self.kwargs['id']
        print(id)
        print(self.request.user.username)
        
        prod=Product.objects.get(id=self.kwargs['id'])
        prods=Product.objects.filter(category=prod.category)
        author=User.objects.get(username = self.request.user)
        if Cart.objects.filter(author=author,product=prod):
           cart=Cart.objects.filter(author=author,product=prod)
        else:
            cart=''
        pdt={
        'user':author,
        'cart':cart,
        'prod':prod,
        'prods':prods,
         }
        return render(request,'buyer/productview.html',pdt)

    def post(self,request):
        if request.method =="POST":
            form = ProductSearchForm(request.POST)
            if form.is_valid():
                psearch=form.cleaned_data['search']
                sprod=Product.objects.filter(name__icontains=psearch)
                pdt={
                    'sprod':sprod,
                }
                return render(request,"buyer/product_search.html",pdt)
        else:
            return redirect("buyer/productlist")

class addCart(GroupRequiredMixin, View):
    group_required = u"buyer"
    def get(self, request, *args, **kwargs):
        author=User.objects.get(username=self.request.user)
        product=Product.objects.get(id = self.kwargs['id'])
        if Cart.objects.filter(author=author,product=product):
            cart=True
        else:
            cart=False
            crt=Cart(product=product,author=author)
            id = product.id
        return redirect('/buyer/productview/%d' %id ,cart)

class viewCart(GroupRequiredMixin, View):
    group_required = u"buyer"
    def get(self, request, *args, **kwargs):
        author=User.objects.get(username=self.request.user)
        if Cart.objects.filter(author=author):
            pcart=Cart.objects.filter(author=author)
        else: 
            pcart=''

        pdt={
                'pcart':pcart,
            }
        return render(request,'buyer/viewcart.html',pdt)
    def post(self,request):
        if request.method =="POST":
            form = ProductSearchForm(request.POST)
            if form.is_valid():
                psearch=form.cleaned_data['search']
                sprod=Product.objects.filter(name__icontains=psearch)
                pdt={
                    'sprod':sprod,
                }
                return render(request,"buyer/product_search.html",pdt)
        else:
            return redirect("buyer/productlist")



class allProducts(GroupRequiredMixin, View):
    group_required = u"buyer"
    def get(self, request, *args, **kwargs):
        prod=Product.objects.filter(category=self.kwargs['name'])
        pdt={
                'prod':prod,
            }
        return render(request,"buyer/allproducts.html",pdt)
    def post(self,request):
        if request.method =="POST":
            form = ProductSearchForm(request.POST)
            if form.is_valid():
                psearch=form.cleaned_data['search']
                sprod=Product.objects.filter(name__icontains=psearch)
                pdt={
                    'sprod':sprod,
                }
                return render(request,"buyer/product_search.html",pdt)
        else:
            return redirect("buyer/productlist")

class orderProduct(GroupRequiredMixin, View):
    group_required = u"buyer"
    def get(self, request, *args, **kwargs): 
        author=User.objects.get(username=self.request.user)
        prod=Product.objects.get(id=self.kwargs['id'])
        prods=Product.objects.filter(category=prod.category)
        if Cart.objects.filter(author=author,product=prod):
            cart=Cart.objects.filter(author=author,product=prod)
        else:
            cart=''
        pdt={
        'cart':cart,
        'prod':prod,
        'prods':prods,
        }
        return render(request,"buyer/placeorder.html",pdt)

    def post(self, request, *args, **kwargs):
         if request.method=="POST":
            name=self.request.POST["name"]
            address=self.request.POST["address"]
            phone=self.request.POST["phone"]
            zip=self.request.POST["zip"]
            prod=Product.objects.get(id=self.kwargs['id'])
            buyer=User.objects.get(username=self.request.user)
            seller=prod.author
            order=Order(name=name,address=address,phone=phone,zip=zip,product=prod,buyer=buyer,seller=prod.author)
            print(order)
            order.save()
            prod.stock=prod.stock - 1
            prod.save()
            
            # subject = 'shoppie'
            # message = 'you have placed your order to %s'%name+' address %s'%address
            # recepient = author.email

            # send_mail(subject,message, EMAIL_HOST_USER, [recepient], fail_silently = False)
            return redirect("/buyer/myorders/")


class myOrders(GroupRequiredMixin, View):
    group_required = u"buyer"
    def get(self, request, *args, **kwargs):
        buyer=User.objects.get(username=self.request.user)
        prods=Product.objects.all()[:4]
        if Order.objects.filter(buyer=buyer):
            oprod=Order.objects.filter(buyer=buyer)
        else:
            oprod=''
        pdt={
            'oprod':oprod,
            'prods':prods,
        }
        return render(request,"buyer/myorder.html",pdt)
    def post(self,request):
        if request.method =="POST":
            form = ProductSearchForm(request.POST)
            if form.is_valid():
                psearch=form.cleaned_data['search']
                sprod=Product.objects.filter(name__icontains=psearch)
                pdt={
                    'sprod':sprod,
                }
                return render(request,"buyer/product_search.html",pdt)
        else:
            return redirect("buyer/productlist")


    
def productsearch(request, form):
    pass
    # form = ProductSearchForm(request.POST)
    # if form.is_valid():
    # psearch=form.cleaned_data['search']
    # sprod=Product.objects.filter(name__icontains=psearch)
    # pdt={
    #     'sprod':sprod,
    #     }
    # return render(request,"buyer/product_search.html",pdt)

    # psearch=form.cleaned_data['search']
    # print(psearch)
    # if request.method =="POST":
    #     print("request")
    #     psearch=request.method["search"]
    # sprod=Product.objects.filter(name__icontains=psearch)
    # pdt={
    #     'sprod':sprod,
    # }
    # return render(request,"buyer/product_search.html",pdt)
    # return redirect("/buyer/productlist")


