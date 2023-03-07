from django.contrib.auth.models import User
from rest_framework import routers, serializers, viewsets

# Create your views here.

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta():
        model = User
        fields = [
            'url', 'username', 'is_staff'
        ]