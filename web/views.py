from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import forms
from django.contrib.auth.mixins import LoginRequiredMixin
from django.forms import ModelForm
from django.shortcuts import render, redirect
from django.urls import reverse, reverse_lazy
from django.http import HttpResponseRedirect
from django.views.generic import CreateView
from rest_framework.permissions import IsAuthenticated

from .models import Sport, Athlete, ScheduleItem, User
from django.views.generic import ListView, TemplateView
from django.contrib.auth.forms import UserCreationForm
from rest_framework.generics import ListAPIView, RetrieveAPIView
from .serializers import SportSerializer, AthleteSerializer
from django.core.mail import send_mail
from olimpiColombia.settings import EMAIL_HOST_USER


class HomeView(TemplateView):
    template_name = 'home.html'


class IndexView(ListView):
    model = Sport
    template_name = 'index.html'


class UserForm(UserCreationForm):
    username = forms.CharField(max_length=50)
    first_name = forms.CharField(max_length=20)
    last_name = forms.CharField(max_length=20)
    email = forms.EmailField()
    password1 = forms.CharField(widget=forms.PasswordInput)
    password2 = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = [
            'username',
            'first_name',
            'last_name',
            'email',
            'password1',
            'password2'
        ]

    def clean_username(self):
        """Comprueba que no exista un username igual en la BD"""
        username = self.cleaned_data['username']
        if User.objects.filter(username=username):
            raise forms.ValidationError('Nombre de usuario ya registrado.')
        return username

    def clean_email(self):
        """Comprueba que no exista un email igual en la BD"""
        email = self.cleaned_data['email']
        if User.objects.filter(email=email):
            raise forms.ValidationError('Ya existe un email igual registrado.')
        return email

    def clean_password2(self):
        """Comprueba que password y password2 sean iguales"""
        password1 = self.cleaned_data['password1']
        password2 = self.cleaned_data['password2']
        if password1 != password2:
            raise forms.ValidationError('Las claves no coinciden.')
        return password2


class UserCreate(CreateView):
    model = User
    template_name = 'userRegistry.html'
    form_class = UserForm
    success_url = '/login/'


class AthletesBySportList(LoginRequiredMixin, ListView):
    model = Athlete
    template_name = 'athletes_by_sport.html'
    context_object_name = 'athletes'

    login_url = '/login/'
    redirect_field_name = 'redirect_to'

    def get_queryset(self, **kwargs):
        sport = self.kwargs['sport_name']
        print(sport)
        queryset = Athlete.objects.filter(sport__name__iexact=sport)
        return queryset


class ScheduleList(LoginRequiredMixin, ListView):
    model = ScheduleItem
    template_name = 'schedule.html'
    context_object_name = 'schedules'

    login_url = '/login/'
    redirect_field_name = 'redirect_to'

    def get_queryset(self, **kwargs):
        athleteId = self.kwargs['athlete_id']
        queryset = ScheduleItem.objects.filter(athlete__pk=athleteId)
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
            send_mail('Olimpicolombia test',
                      'This a test for olimpi colombia project',
                      EMAIL_HOST_USER,
                      ['rtaimal@gmail.com'],
                      fail_silently=True)
            mensaje = 'Nombre de usuario o clave no valida. Usuario: ' + str(username) + ", clave: " + str(password)

    return render(request, 'login.html', {'mensaje': mensaje})


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))


class SportListView(ListAPIView):
    serializer_class = SportSerializer
    queryset = Sport.objects.all()

    # permission_classes = (IsAuthenticated,)


class AthleteBySportListView(ListAPIView):
    serializer_class = AthleteSerializer

    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        athletes = Athlete.objects.filter(
            sport__name__iexact=self.kwargs['sport_name'])
        return athletes
