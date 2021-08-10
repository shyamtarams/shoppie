from django.shortcuts import render
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
    prod=Product.objects.get(id=id)
    print(prod)
    pdt={
        'prod':prod,
    }
    return render(request,'buyer/productview.html',pdt)
