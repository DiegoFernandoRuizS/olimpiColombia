from django.conf.urls import url
from .views import IndexView,AthleteView
from web import views

urlpatterns = [
    url(r'^$', IndexView.as_view(), name='index'),
    url(r'^athlete/$', AthleteView.as_view(), name='athlete'),

]