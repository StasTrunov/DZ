from django.shortcuts import render
from school.models import Student,Class,School
from school.serializer import StudentSerializer
from rest_framework import permissions, viewsets

# Create your views here.


class StudentView(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    permissions_classes = [
        permissions.IsAuthenticated
    ]
