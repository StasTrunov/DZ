from django.contrib.auth.models import User
from rest_framework import routers, serializers, viewsets

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = [
            'url', 'username', 'is_staff'
        ]



class CategorySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = [
            'id', 'name'
        ] 


class PostSerializer(serializers.HyperlinkedModelSerializer):
    category=CategorySerializer
    class Meta:
        model = User
        fields = [
            'id', 'author', 'like', 'dislike', 'text', 'date', 'donate', 'categpry'
        ]