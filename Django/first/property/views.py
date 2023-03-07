from django.shortcuts import render
from property.models import Mail, Account, Game
from property.serializer import AccountSerializer
from rest_framework import permissions, viewsets

# Create your views here.


class AccountView(viewsets.ModelViewSet):
    queryset = Account.objects.all()
    serializer_class = AccountSerializer
    permissions_classes = [
        permissions.IsAuthenticated
    ]
