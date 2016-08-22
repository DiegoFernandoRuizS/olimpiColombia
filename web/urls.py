from django.conf.urls import url
from .views import IndexView, AthletesBySportList

urlpatterns = [
    url(r'^$', IndexView.as_view(), name='index'),
    url(r'^athletes_by_sport/(?P<sport_name>\w+)', AthletesBySportList.as_view(), name='athletes_by_sport'),
]