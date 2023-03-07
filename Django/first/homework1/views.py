from django.shortcuts import render
from homework1.models import FPlayer,FClub,Championship
from homework1.serializer import FPlayerSerializer
from rest_framework import permissions, viewsets

# Create your views here.


class FPlayerView(viewsets.ModelViewSet):
    queryset = FPlayer.objects.all()
    serializer_class = FPlayerSerializer
    permissions_classes = [
        permissions.IsAuthenticated
    ]
