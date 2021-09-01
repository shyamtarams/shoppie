from django.contrib import admin
from django.urls import path,include
from . import views
from accounts.views import *
from .views import addProduct

urlpatterns = [
    # path('guest',views.guest,name='guest'),
    # path('home',views.home,name='home'),
    path('test',test,name='test'),
    path('testh',views.testh,name='testh'),
    path('sellerhome',views.sellerHome,name='sellerHome'),
    path('addproduct',addProduct.as_view(),name='addProduct'),
    path('deleteproduct/<int:id>',views.deleteProduct),
    path('myorders',views.orders),
    path('confirmorder/<int:id>',views.confirmorder),

]