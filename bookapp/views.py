from django.shortcuts import render
from django.views.generic import ListView
from .models import Books


# Create your views here.

class BookView(ListView):
    model = Books
    template_name = 'book_list.html'