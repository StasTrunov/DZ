from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from snippets.models import Snippet
from snippets.serializers import SnippetSerializer
from snippets.models import STYLES_CHOICES, LANGUAGE_CHOICES
from rest_framework import status
from rest_framework.response import Response

# Create your views here.
@csrf_exempt
def snippets_list(request):
    if request.method == "GET":
        snippets = Snippet.objects.all()
        serializer = SnippetSerializer(snippets, many=True)
        return JsonResponse(serializer.data, status=200, safe=False)
    elif request.method == "POST":
        data = JSONParser().parse(request)
        serializer = SnippetSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=200)
        return JsonResponse(serializer.errors, status=400)

@csrf_exempt
def snippet_detail(request, pk):
    try:
        snippet = Snippet.objects.get(id=pk)
    except Snippet.DoesNotExist:
        return Response("DoesNotExist", status=status.HTTP_404_NOT_FOUND)
    if request.method == "GET":
        serializer = SnippetSerializer(snippet)
        return Response(serializer.data, status=status.HTTP_200_OK)
    elif request.method == "PUT":
        serializer = SnippetSerializer(snippet, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@csrf_exempt
def styles_list(request):
    if request.method == "GET":
        return JsonResponse(STYLES_CHOICES, status=200, safe=False)
    else:
        return HttpResponse('invalid method')

@csrf_exempt   
def language_list(request):
    if request.method == "GET":
        return JsonResponse(LANGUAGE_CHOICES, status=200, safe=False)
    else:
        return HttpResponse('invalid method')