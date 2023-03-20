from django.contrib.auth.models import User
from school.models import School, Student, Class
from rest_framework import serializers, routers, viewsets

# Create your views here.
class StudentSerializer(serializers.HyperlinkedModelSerializer):
    class Meta():
        model = Student
        fields = [
            'name', 'second_name', 'email', 'age'
        ]