from django.shortcuts import render
from django.conf.urls import url

from . import views


urlpatterns = [
   url(r'^$', views.index, name='index'),
   url('/health/', views.health, name='health')
]