from django.shortcuts import render
from .models import Sport, Athlete, ScheduleItem
from django.views.generic import ListView, TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin

class IndexView (ListView):
    model = Sport
    template_name = 'index.html'


class LoginView(TemplateView):
    template_name = "login.html"


class AthletesBySportList(LoginRequiredMixin, ListView):
    model = Athlete
    template_name = 'athletes_by_sport.html'
    context_object_name = 'athletes'
    login_url = 'login'
    redirect_field_name = 'redirect_to'
    # paginate_by = 10

    def get_queryset(self, **kwargs):
        sport = self.kwargs['sport_name']
        print(sport)
        queryset = Athlete.objects.filter(sport__name__exact = sport)
        return queryset


class ScheduleList(LoginRequiredMixin, ListView):
    model = ScheduleItem
    template_name = 'schedule.html'
    context_object_name = 'schedules'
    login_url = 'login'
    redirect_field_name = 'redirect_to'

    # paginate_by = 10

    def get_queryset(self, **kwargs):
        athleteId = self.kwargs['athlete_id']
        queryset = ScheduleItem.objects.filter(athlete__identification=athleteId)
        return queryset
