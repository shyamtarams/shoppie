from django.contrib import admin
from django.urls import path,include
from . import views
from django.contrib.auth.views import LoginView

#rest api imports
from rest_framework import routers
router = routers.DefaultRouter()

#routers
# router.register(r'login', views.UserViewSet,'login'),


urlpatterns = [
    path('signup',views.signup,name='signup'),
    path('login',LoginView.as_view(),name='login'),
    # path('dashboard',views.dashboard,name='dashboard'),
    path('',include('django.contrib.auth.urls')),
    path('guest',views.guest,name='guest'),
    # path('test',views.test,name='test'),
    path('sellersignup',views.sellersignup,name='sellersignup'),
    path('verify',views.verify,name='verify'),
    path('check',views.check,name='check'),
    path('CompanyRegister',views.sellerCompanyRegister,name='sellerCompanyRegister'),
    #api 
    # path('api/', include(router.urls)),
    path('lg/',views.validate, name="lg"),
]