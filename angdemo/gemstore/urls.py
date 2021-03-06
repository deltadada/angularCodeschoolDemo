
from django.conf.urls import url
from django.contrib import admin
from . import views

urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^home/$', views.home, name='home'),
    url(r'^django_display/$', views.django_display, name='django_display'),
    url(r'^angular_display/$', views.angular_display, name='angular_display'),
    url(r'^gemapi/gemsthumb_list/$', views.gemsthumb_list, name='buygems'),
    url(r'^gemapi/gems_list/$', views.gems_list, name='allgems'),
    url(r'^gemapi/availableGemsThumbs_list/$', views.availableGemsThumbs_list, name='availableGems'),
    url(r'^test/$', views.test, name='test'),
]

