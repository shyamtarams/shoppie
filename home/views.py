from django.shortcuts import render,redirect
from .forms import *
from django.views.generic import ListView, CreateView
from django.urls import reverse_lazy
from buyer.models import *
from django.contrib.auth.models import User


from braces.views import GroupRequiredMixin

# send mail
from shoppie.settings import EMAIL_HOST_USER
from django.core.mail import send_mail



from django.contrib.auth.models import User
# Create your views here.

# def guest(request):
#     return render(request,"guest_home.html")

def home(request):
    return render(request,"home/home.html")

def testh(request):
    return render(request,"home/test.html")


def sellerHome(request):
    user=request.user
    user=User.objects.get(username=user)
    plst=""
    pcnt=""
    ocnt=""
    if Order.objects.filter(seller=user):
        ocnt=Order.objects.filter(seller=user).count()

    if request.method=="POST":
        sr=request.POST["search"]
        plst=Product.objects.filter(name__icontains=sr)
        pcnt=Product.objects.filter(author=user).count()
        pdt={
            'ocnt':ocnt,
            'user':user,
            'plst':plst,
            'pcnt':pcnt,
        }
        return render(request,"seller/dashboard.html",pdt)

    

    if Product.objects.filter(author=user):
        plst=Product.objects.filter(author=user).order_by('-date')
        pcnt=Product.objects.filter(author=user).count()
        pdt={
            'ocnt':ocnt,
            'user':user,
            'plst':plst,
            'pcnt':pcnt,
        }
        return render(request,"seller/dashboard.html",pdt)
        
    pdt={
        'user':user,
    }
    return render(request,"seller/dashboard.html",pdt)


def deleteProduct(request,id):
    Product.objects.get(id=id).delete()
    return redirect('/sellerhome')

class addProduct(GroupRequiredMixin,CreateView):
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

def orders(request):
    user=request.user
    user=User.objects.get(username=user)
    # seller=Product.objects.get()
    order=Order.objects.filter(seller=user)
    sell={
        'order':order,
    }

    return render(request,"seller/myorders.html",sell)

def confirmorder(request,id):
    if request.method=="POST":
        order=Order.objects.get(id=id)
        ddate=request.POST["date"]
        if order.buyer.email:
            name=order.product.name
            address=order.address
            subject = 'shoppie-delivery'
            message = 'you have placed your order to %s'%name+' address %s'%address+' will be delivered on or before %s'%ddate
            recepient = order.buyer.email
            send_mail(subject,message, EMAIL_HOST_USER, [recepient], fail_silently = False)
        else:
            print("no mail")
    return redirect("/myorders")

# def productsearch(request,name):
#     print(name)
#     return redirect("/sellerhome")

def updateproduct(request,id):
    cat=Category.objects.all()
    pdt=Product.objects.get(id=id)
    user=request.user
    user=User.objects.get(username=user)
    if request.method=="POST":
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
        # update_product.save()
        # print(update_product)
        return redirect("/updateproduct/%d"%id)
    else:
        pdt={
            'cat':cat,
            'pdt':pdt,
        }
        return render(request,"seller/updateproduct.html",pdt)





    

    


    


    

