from django.shortcuts import render
from .models import Sport, Athlete, ScheduleItem
from django.views.generic import ListView, TemplateView


class IndexView (ListView):
    model = Sport
    template_name = 'index.html'


class LoginView(TemplateView):
    template_name = "login.html"


class AthletesBySportList(ListView):
    model = Athlete
    template_name = 'athletes_by_sport.html'
    context_object_name = 'athletes'

    # paginate_by = 10

    def get_queryset(self, **kwargs):
        sport = self.kwargs['sport_name']
        print(sport)
        queryset = Athlete.objects.filter(sport__name__exact = sport)
        return queryset


class ScheduleList(ListView):
    model = ScheduleItem
    template_name = 'schedule.html'
    context_object_name = 'schedules'

    # paginate_by = 10

    def get_queryset(self, **kwargs):
        athleteId = self.kwargs['athlete_id']
        queryset = ScheduleItem.objects.filter(athlete__identification=athleteId)
        return queryset
