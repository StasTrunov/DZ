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

class ClassSerializer(serializers.HyperlinkedModelSerializer):
    class Meta():
        model = Class
        fields = [
            'name', 'age'
        ]

class SchoolSerializer(serializers.HyperlinkedModelSerializer):
    class Meta():
        model = School
        fields = [
            'name', 'country'
        ]