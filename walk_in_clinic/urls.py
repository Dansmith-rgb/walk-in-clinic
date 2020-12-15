"""Defines url patterns for walk-in-clinic"""

from django.urls import path

from . import views

app_name = 'walk_in_clinic'
urlpatterns = [
    # Home page
    path('', views.index, name='index'),
    # Page that shows all appointments
    path('appointments/', views.appointments, name='appointments'),
]