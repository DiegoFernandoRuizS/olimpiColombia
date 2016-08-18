from django.shortcuts import render
from .models import Sport
from django.views.generic.list import ListView

class IndexView (ListView):
    model = Sport
    template_name = 'index.html'
