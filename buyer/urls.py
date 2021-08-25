from django.urls import path,include
from . import views


urlpatterns = [
    path('productlist',views.buyerHome,name="buyerHome"),
    path('productview/<int:id>',views.productView,name="productView"),
    path('addcart/<int:id>',views.addCart,name="addCart"),
    path('viewcart',views.viewCart,name="addCart"),
]