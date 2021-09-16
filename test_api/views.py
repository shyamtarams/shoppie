from django.shortcuts import render
from rest_framework import viewsets
from .serializers import HerosSerializer
from .models import Heros
from rest_framework import routers

# Create your views here.

class HerosViewSet(viewsets.ModelViewSet):
# class HerosViewSet(generics.ListAPIView):
    queryset = Heros.objects.all().order_by('name')
    serializer_class = HerosSerializer