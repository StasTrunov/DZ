from django.contrib.auth.models import User
from homework1.models import FClub,FPlayer,Championship
from rest_framework import serializers, routers, viewsets

# Create your views here.
class FPlayerSerializer(serializers.HyperlinkedModelSerializer):
    class Meta():
        model = FPlayer
        fields = [
            'login', 'costs', 'height', 'country'
        ]