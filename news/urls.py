from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from news import views

urlpatterns = [
    path('', views.news, name='news'),

]