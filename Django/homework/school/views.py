from django.shortcuts import render
from django.http import HttpResponse, JsonResponse, Http404
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from school.models import Student, Class, School
from school.serializer import StudentSerializer, ClassSerializer, SchoolSerializer
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework import permissions
from rest_framework.views import APIView


# Create your views here.
@csrf_exempt
def students_list(request):
    if request.method == "GET":
        snippets = Student.objects.all()
        serializer = StudentSerializer(snippets, many=True)
        return JsonResponse(serializer.data, status=200, safe=False)
    elif request.method == "POST":
        data = JSONParser().parse(request)
        serializer = StudentSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=200)
        return JsonResponse(serializer.errors, status=400)


@api_view(["GET", "POST", "PUT", "DELETE"])
@permission_classes((permissions.AllowAny,))
def student_detail(request, pk):
    try:
        student = Student.objects.get(id=pk)  
    except Student.DoesNotExist:
        return JsonResponse("DoesNotExist", status=status.HTTP_404_NOT_FOUND)
    if request.method == "GET":
        serializer = StudentSerializer(student)
        return JsonResponse(serializer.data, status=status.HTTP_200_OK)
    elif request.method == "POST":
        serializer = StudentSerializer(data=request.data)
        return JsonResponse(serializer.data, status = status.HTTP_200_OK)
    elif request.method == "PUT":
        # print(request)
        serializer = StudentSerializer(student, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=status.HTTP_200_OK)
        return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == "DELETE":
        student.delete()
        return JsonResponse('delete',status=status.HTTP_204_NO_CONTENT)
    


@csrf_exempt
def classes_list(request):
    if request.method == "GET":
        classes = Class.objects.all()
        serializer = ClassSerializer(classes, many=True)
        return JsonResponse(serializer.data, status=200, safe=False)
    elif request.method == "POST":
        data = JSONParser().parse(request)
        serializer = ClassSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=200)
        return JsonResponse(serializer.errors, status=400)
    


@api_view(["GET", "PUT", "DELETE"])
@permission_classes((permissions.AllowAny,))
def school_detail(request, pk):
    try:
        student = School.objects.get(id=pk)  
    except School.DoesNotExist:
        return JsonResponse("DoesNotExist", status=status.HTTP_404_NOT_FOUND)
    if request.method == "GET":
        serializer = SchoolSerializer(student)
        return JsonResponse(serializer.data, status=status.HTTP_200_OK)
    elif request.method == "PUT":
        # print(request)
        serializer = SchoolSerializer(student, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=status.HTTP_200_OK)
        return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == "DELETE":
        student.delete()
        return JsonResponse('delete',status=status.HTTP_204_NO_CONTENT)