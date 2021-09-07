from django.contrib import admin
from django.urls import path,include
from . import views
from accounts.views import *
from .views import addProduct,orderList,sellerHome

from rest_framework import routers

router = routers.DefaultRouter()
# router.register(r'users', views.UserViewSet)
router.register(r'category', views.CategoryViewSet,'Category')

urlpatterns = [
    # path('guest',views.guest,name='guest'),
    # path('home',views.home,name='home'),
    path('test',test,name='test'),
    path('testh',views.testh,name='testh'),
    # path('sellerhome',views.sellerHome,name='sellerHome'),
    path('sellerhome',sellerHome.as_view(),name='sellerHome'),
    path('addproduct',addProduct.as_view(),name='addProduct'),
    path('deleteproduct/<int:id>',views.deleteProduct),
    # path('myorders',views.orders),
    path('myorders',orderList.as_view(),name='myorders'),
    path('confirmorder/<int:id>',views.confirmorder),
    # path('productsearch/<str:name>',views.productsearch),
    path('updateproduct/<int:id>',views.updateproduct),
    #rest api urls
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('api/', include(router.urls)),
     
]