from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('view/<int:pk>/', views.ViewArticle, name='view'),
    path('create/', views.createArticle, name='create')
]