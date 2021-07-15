from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path("",views.home, name='home'),
    path("info", views.info, name='info'),
    path("contact", views.contact, name='info')

]
