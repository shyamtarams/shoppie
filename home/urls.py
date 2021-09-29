from django.contrib import admin
from django.urls import path,include
from . import views
from accounts.views import *
from .views import addProduct,orderList,sellerHomes
# from .views import *

from . import apiview

from rest_framework import routers

router = routers.DefaultRouter()
# router.register(r'users', views.UserViewSet)
router.register(r'category', apiview.CategoryViewSet,'Category'),
router.register(r'offer', apiview.OfferViewSet, 'Offer'),
router.register(r'product', apiview.ProductViewSet, 'product'),
router.register(r'cart', apiview.ProductCartViewSet, 'cart'),

urlpatterns = [
    path('test',test,name='test'),
    path('testh',views.testh,name='testh'),
    path('sellerhome/',sellerHomes.as_view(),name='sellerHomes'),
    path('addproduct',addProduct.as_view(),name='addProduct'),
    path('deleteproduct/<int:id>',views.deleteProduct),
    path('myorders',orderList.as_view(),name='myorders'),
    path('confirmorder/<int:id>',views.confirmOrder.as_view(),name='confirmOrder'),
    path('updateproduct/<int:id>',views.updateProduct.as_view(),name='updateProduct'),
    #rest api urls
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('api/', include(router.urls)),
    #function based
    path('prod/',apiview.postpro,name='prod'),
    path('update/',apiview.uppro,name='update'),
    path('delete/',apiview.dlpro,name='delete'),
     
]