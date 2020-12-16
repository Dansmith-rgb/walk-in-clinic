"""Defines url patterns for walk-in-clinic"""

from django.urls import path

from . import views

app_name = 'walk_in_clinic'
urlpatterns = [
    # Home page
    path('', views.index, name='index'),
    # Page that shows all appointments
    path('appointments/', views.appointments, name='appointments'),
    # Detail page for single appointments
    path('appointments/<int:appointment_id>/', views.appointment, name='appointment'),
    # Page for adding new appointment
    path('new_appointment/', views.new_appointment, name='new_appointment'),
]