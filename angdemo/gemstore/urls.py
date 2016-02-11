
from django.conf.urls import url
from django.contrib import admin
from . import views

urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^home/$', views.home, name='home'),
    url(r'^django_display/$', views.django_db_dump, name='django_display'),
    url(r'^dump/$', views.django_db_dump, name='dump'),
    url(r'^test/$', views.test, name='test'),
]

