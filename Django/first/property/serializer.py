from django.contrib.auth.models import User
from property.models import Mail, Account, Game
from rest_framework import serializers, routers, viewsets

# Create your views here.
class AccountSerializer(serializers.HyperlinkedModelSerializer):
    class Meta():
        model = Account
        fields = [
            'login', 'costs', 'password', 'description'
        ]
