from django.shortcuts import render,redirect
from .forms import *
from django.views.generic import ListView, CreateView
from django.urls import reverse_lazy


from braces.views import GroupRequiredMixin
from django.views.generic import TemplateView

class SomeProtectedView(GroupRequiredMixin, TemplateView):

    #required
    group_required = u"editors"

    def check_membership(self, group):
    
        # Check some other system for group membership
        if user_in_group:
            print("true")
        else:
            print("false")


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
    if Product.objects.filter(author=user):
        plst=Product.objects.filter(author=user).order_by('-date')
        pcnt=Product.objects.filter(author=user).count()
        pdt={
            'user':user,
            'plst':plst,
            'pcnt':pcnt,
        }
    pdt={
        'user':user,
    }
    return render(request,"seller/dashboard.html",pdt)

def Product(request):
    print(request.user)
    user=request.user
    auth=User.objects.get(username=user)
    f=auth.id
    print(f)

    if request.method == 'POST':
        form = AddProductForm(request.POST, request.FILES)
        print(form.is_valid())
        print(form)
        # nm = form.cleaned_data['name']
        # print(nm)
        
        if form.is_valid():
            f=form.save(commit=False)
            print("-----------")
            user=request.user
            auth=User.objects.get(username=user)
            f.author=auth
            # form.cleaned_data['author_id']=auth.id
            # print(type(form))
            # print("----------------------adding auth")
            # print(form.cleaned_data)
            f.save()
            return redirect('/sellerhome')
    else:
        form = AddProductForm()
    cat=Category.objects.all()
    return render(request,"seller/addproduct.html", {'form': form,'cat':cat})

class addProduct(GroupRequiredMixin,CreateView):
    group_required = u"sellers"
    model = Product
    form_class = AddProductForm
    template_name = 'seller/addproduct.html'
    success_url = reverse_lazy('addproduct')
    def form_valid(self, form):
        f = form.save(commit=False)
        f.author = self.request.user
        f.save()
        return super(addproduct, self).form_valid(form)



    


    

