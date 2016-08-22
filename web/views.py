from django.shortcuts import render
from .models import Sport, Athlete
from django.views.generic.list import ListView

class IndexView (ListView):
    model = Sport
    template_name = 'index.html'


class AthletesBySportList(ListView):
    model = Athlete
    template_name = 'athletes_by_sport.html'
    context_object_name = 'athletes'

    # paginate_by = 10

    def get_queryset(self, **kwargs):
        sport = self.kwargs['sport_name']
        queryset = Athlete.objects.filter(sport__name__icontains = sport)
        return queryset