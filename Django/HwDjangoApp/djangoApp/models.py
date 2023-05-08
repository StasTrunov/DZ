from django.db import models

# Create your models here.

class Article(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=1000)
    body = models.CharField(max_length=20000)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)
