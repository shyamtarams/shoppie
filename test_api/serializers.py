# from django.contrib.auth.models import User, Group
from .models import Heros
from rest_framework import serializers

class HerosSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Heros
        # fields = ['name', 'price']
        fields ="__all__"