from django.urls import path,include
from rest_framework import routers
from .models import Heros
from .serializers import HerosSerializer
from . import views 


router = routers.DefaultRouter()
router.register(r'heros', views.HerosViewSet,basename='Heros')

urlpatterns = [
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('api/', include(router.urls)),
    # path('heros/',as_view())
]
