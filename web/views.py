from django.contrib.auth.mixins import LoginRequiredMixin
from django.forms import ModelForm
from django.shortcuts import render, redirect
from django.urls import reverse
from django.urls import reverse_lazy
from django.http import HttpResponseRedirect
from django.views.generic import CreateView
from .models import Sport, Athlete, ScheduleItem


class UserCreate(CreateView):
    model = User
    template_name = 'userRegistry.html'
    form_class = UserForm
    success_url = reverse_lazy('add_user')
    # https://simpleisbetterthancomplex.com/tutorial/2016/07/22/how-to-extend-django-user-model.html


class IndexView (ListView):
    model = Sport
    template_name = 'index.html'


class AthletesBySportList(LoginRequiredMixin, ListView):
    model = Athlete
    template_name = 'athletes_by_sport.html'
    context_object_name = 'athletes'

    login_url = '/login/'
    redirect_field_name = 'redirect_to'

    def get_queryset(self, **kwargs):
        sport = self.kwargs['sport_name']
        print(sport)
        queryset = Athlete.objects.filter(sport__name__exact = sport)
        return queryset


class ScheduleList(LoginRequiredMixin, ListView):
    model = ScheduleItem
    template_name = 'schedule.html'
    context_object_name = 'schedules'

    login_url = '/login/'
    redirect_field_name = 'redirect_to'

    def get_queryset(self, **kwargs):
        athleteId = self.kwargs['athlete_id']
        queryset = ScheduleItem.objects.filter(athlete__identification=athleteId)
        return queryset


def login_view(request):
    if request.user.is_authenticated():
        return redirect(reverse('index'))

    mensaje = ''
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect(reverse('index'))
        else:
            mensaje = 'Nombre de usuario o clave no valida. Usuario: ' + str(username) + ", clave: " + str(password)

    return render(request, 'login.html', {'mensaje': mensaje})


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse('images:index'))