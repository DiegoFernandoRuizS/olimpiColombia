from django.conf.urls import url, include
from . import views
from .views import (HomeView, IndexView, AthletesBySportList, ScheduleList, UserCreate,
                    SportListView, AthleteBySportListView)

urlpatterns = [
    url('', include('social.apps.django_app.urls', namespace='social')),
    url(r'^$', HomeView.as_view(), name='home'),
    url(r'^home/$', IndexView.as_view(), name='index'),
    url(
        r'^athletes_by_sport/(?P<sport_name>[^/]+)/$',
        AthletesBySportList.as_view(),
        name='athletes_by_sport'
    ),
    url(
        r'^schedules/(?P<athlete_id>\w+)',
        ScheduleList.as_view(),
        name='schedule_by_athlete'
    ),
    url(r'^add_user/', UserCreate.as_view(), name='add_user'),
    url(r'^login/$', views.login_view, name='login'),
    url(r'^logout/$', views.logout_view, name='logout'),
    url(r'^api/sports/', SportListView.as_view(), name='sports-list'),
    url(
        r'^api/athletes_by_sport/(?P<sport_name>[^/]+)/$',
        AthleteBySportListView.as_view(),
    ),
]
