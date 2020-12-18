"""Defines url patterns for walk-in-clinic"""

from django.urls import path

from . import views

app_name = 'walk_in_clinic'
urlpatterns = [
    # Home page
    path('', views.index, name='index'),
    # Page that shows all appointments
    path('appointments/', views.appointments, name='appointments'),
    # Page that shows all appointments for dr
    path('appointments_dr/', views.appointments_dr, name='appointments_dr'),
    # Detail page for single appointments
    path('appointments/<int:appointment_id>/', views.appointment, name='appointment'),
    # Page for the dr to see a single appointment
    path('appointments_dr/<int:appointment_id>/', views.appointment_dr, name='appointment_dr'),
    # Page for adding new appointment
    path('new_appointment/', views.new_appointment, name='new_appointment'),
    # Page for editing appointments
    path('edit_appointment/<int:appointment_id>/', views.edit_appointment, name="edit_appointment"),
    # Page for seeing all clinics
    path('clinics/', views.clinics, name='clinics'),
    # Page for seeing a single clinic
    path('clinics/<int:clinic_id>/', views.clinic, name='clinic'),
    # Page for dr to make a clinic
    path('new_clinic/', views.new_clinic, name='new_clinic'),
    # Page for dr to edit clinic
    path('edit_clinic/<int:clinic_id>/', views.edit_clinic, name='edit_clinic')
]