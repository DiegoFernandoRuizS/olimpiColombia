from django.conf.urls import url
from .views import IndexView, AthletesBySportList, ScheduleList

urlpatterns = [
    url(r'^$', IndexView.as_view(), name='index'),
    url(r'^athletes_by_sport/(?P<sport_name>\w+)', AthletesBySportList.as_view(), name='athletes_by_sport'),
    url(r'^schedules/', ScheduleList.as_view(), name='schedule'),
]
