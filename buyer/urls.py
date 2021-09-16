from django.urls import path,include
from . import views


urlpatterns = [
    # path('productlist',views.buyerHome,name="buyerHome"),
    path('productlist',views.buyerhome.as_view(),name="buyerhome"),
    path('productview/<int:id>',views.productview.as_view(),name="productview"),
    path('addcart/<int:id>',views.addCart.as_view(),name="addCart"),
    path('viewcart',views.viewCart.as_view(),name="viewCart"),
    path('allproducts/<str:name>',views.allProducts.as_view(),name="allProducts"),
    # path('allproducts/',views.allProducts.as_view(),name="allProducts"),
    path('orderproduct/<int:id>',views.orderProduct.as_view(),name="orderProduct"),
    path('productsearch',views.productsearch,name="productsearch"),
    path('myorder/',views.myOrders.as_view(),name="myOrders"),
]