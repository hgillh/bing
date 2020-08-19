
from django.contrib import admin
from django.conf.urls import include
from django.urls import path
from bingapp import views

urlpatterns = [
    path('bing/', include('bingapp.urls')),
    path('', views.home),
]
