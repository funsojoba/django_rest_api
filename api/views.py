from django.shortcuts import render
from django.views.generic import ListView
from rest_framework import generics

from bookapp.models import Books
from .serializers import BookSerializer

# Create your views here.
class BookAPIView(generics.ListAPIView):
    queryset = Books.objects.all()
    serializer_class = BookSerializer