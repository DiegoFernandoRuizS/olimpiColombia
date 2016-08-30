from django.conf.urls import url, include
from .views import IndexView, AthletesBySportList, ScheduleList, LoginView

urlpatterns = [
    url('', include('social.apps.django_app.urls', namespace='social')),
    url(r'^$', IndexView.as_view(), name='index'),
    url(r'^athletes_by_sport/(?P<sport_name>[^/]+)/$', AthletesBySportList.as_view(), name='athletes_by_sport'),
    url(r'^schedules/(?P<athlete_id>\w+)', ScheduleList.as_view(), name='schedule_by_athlete'),
    url(r'^login/', LoginView.as_view(), name='login'),
    url(r'^complete/google-oauth2', IndexView.as_view(), name='index'),
]
