from django.shortcuts import render, redirect
from .models import Sport, Athlete
from django.views.generic.list import ListView




class IndexView (ListView):
    model = Sport
    template_name = 'index.html'

class AthleteView (ListView):
    model = Athlete
    template_name = 'athlete.html'



