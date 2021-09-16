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

from django.contrib.auth.models import User

# rest api
# from django.contrib.auth.models import User
from rest_framework import viewsets
from rest_framework import permissions
# from .serializers import UserSerializer,CategorySerializer
from .serializers import CategorySerializer, OfferSerializer
from buyer.utils import status

# Create your views here.

# def guest(request):
#     return render(request,"guest_home.html")

def home(request):
    return render(request,"home/home.html")

def testh(request):
    return render(request,"home/test.html")

# class based view
class sellerHomes(GroupRequiredMixin, View):
    group_required = u"sellers"
    def get(self, request):
        User = get_user_model()
        username = self.request.user
        user=User.objects.get(username=username)
        plst=""
        pcnt=""
        ocnt=""
        if Order.objects.filter(seller=user):
            ocnt=Order.objects.filter(seller=user).count()
        if Product.objects.filter(author=user.id):
            plst=Product.objects.filter(author=user.id).order_by('-date')
            pcnt=Product.objects.filter(author=user.id).count()
        pdt={
            'ocnt':ocnt,
            'user':user,
            'plst':plst,
            'pcnt':pcnt,
        }
        return render(self.request,"seller/dashboard.html",pdt)
    
    def post(self,request):
        User = get_user_model()
        username = self.request.user
        user=User.objects.get(username=username)
        plst=""
        pcnt=""
        ocnt=""
        if Order.objects.filter(seller=user):
            ocnt=Order.objects.filter(seller=user).count()
        if Product.objects.filter(author=user.id):
            plst=Product.objects.filter(author=user.id).order_by('-date')
            pcnt=Product.objects.filter(author=user.id).count()
        if self.request.method=="POST":
            sr=request.POST["search"]
            plst=Product.objects.filter(name__icontains=sr)
            pcnt=Product.objects.filter(author=user).count()
        pdt={
            'ocnt':ocnt,
            'user':user,
            'plst':plst,
            'pcnt':pcnt,
        }
        return render(self.request,"seller/dashboard.html",pdt)



def deleteProduct(request,id):
    Product.objects.get(id=id).delete()
    return redirect('/sellerhome')

class addProduct(GroupRequiredMixin,CreateView):
    User = get_user_model()
    group_required = u"sellers"
    model = Product
    form_class = AddProductForm
    template_name = 'seller/addproduct.html'
    success_url = reverse_lazy('addProduct')
    def form_valid(self, form):
        f = form.save(commit=False)
        f.author = self.request.user
        f.save()
        return super(addProduct, self).form_valid(form)

    def get(self,request):
        cat=Category.objects.all()
        return render(request,"seller/addproduct.html", {'cat':cat})


class orderList(GroupRequiredMixin, View):
    group_required = u"sellers"
    def get(self, request):
        User = get_user_model()
        user=request.user
        user=User.objects.get(username=user)
        order=Order.objects.filter(seller=user)
        sell={
                'order':order,
            }
        return render(request,"seller/myorders.html",sell)

class confirmOrder(GroupRequiredMixin, View):
    group_required = u"sellers"
    def post(self, request, *args, **kwargs):
        if self.request.method=="POST":
            print("post")
            order=Order.objects.get(id=self.kwargs['id'])
            ddate=request.POST["date"]
            order.delivary_date=ddate
            order.save()
            if order.buyer.email:
                print(ddate)
                # name=order.product.name
                # address=order.address
                # subject = 'shoppie-delivery'
                # message = 'you have placed your order to %s'%name+' address %s'%address+' will be delivered on or before %s'%ddate
                # recepient = order.buyer.email
                # send_mail(subject,message, EMAIL_HOST_USER, [recepient], fail_silently = False)
            else:
                print("no mail")
        return redirect("/myorders")


class updateProduct(GroupRequiredMixin, View):
    group_required = u"sellers"
    def get(self, request, *args, **kwargs):
        pdt = Product.objects.get(id=self.kwargs['id'])
        cat=Category.objects.all()
        pdt = {
            'pdt':pdt,
            'cat':cat,
        }
        return render(request,"seller/updateproduct.html",pdt)

    def post(self, request, *args, **kwargs):
        pdt = Product.objects.get(id=self.kwargs['id'])
        cat=Category.objects.all()
        user = myUser.objects.get(username=self.request.user)
        if self.request.method == "POST":
            name=request.POST["name"]
            category=request.POST["category"]
            description=request.POST["description"]
            if description:
                description=description
            else:
                description=pdt.description
            if request.FILES:
                product_image=request.FILES["product_image"]
                print(product_image)
            else:
                product_image=pdt.product_image

            price=request.POST["price"]
            if price:
                price=price
            else:
                price=pdt.price

            stock=request.POST["stock"]
            if stock:
                stock=stock
            else:
                stock=pdt.stock

        
            print(name,category,description,stock,price, product_image)
            pdt.name=name
            pdt.category=category
            pdt.description=description
            pdt.product_image=product_image
            pdt.price=price
            pdt.stock=stock
            pdt.author=user
            pdt.save()
            return redirect("/updateproduct/%d"%self.kwargs['id'])
            

# class UserViewSet(viewsets.ModelViewSet):
#     queryset = User.objects.all().order_by('-date_joined')
#     serializer_class = UserSerializer
#     permission_classes = [permissions.IsAuthenticated]

class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all().order_by('name')
    serializer_class = CategorySerializer

class OfferViewSet(viewsets.ModelViewSet):
    queryset = Offer.objects.all()
    serializer_class = OfferSerializer




    

    


    


    

