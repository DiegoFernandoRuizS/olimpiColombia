from django.shortcuts import render
from .models import Sport, Athlete, ScheduleItem
from django.views.generic import ListView, TemplateView

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

class ScheduleList(ListView):
     model = ScheduleItem
     template_name = 'schedule.html'
     context_object_name = 'schedules'


