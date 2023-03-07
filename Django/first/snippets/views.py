from django.shortcuts import render
from snippets.models import Snippet
from snippets.serializers import SnippetSerializer
from django.http import JsonResponse
from rest_framework.parses import JSONParser

# Create your views here.

def snippet_list(request):
    if request.method == 'GET':
        snippets = Snippet.objects.all()
        serializer = SnippetSerializer
        return JsonResponse(serializer.data)
    
    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = SnippetSerializer(data, many = True)

