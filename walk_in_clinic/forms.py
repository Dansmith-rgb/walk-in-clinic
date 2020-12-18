from django import forms

from .models import Appointment, Clinic

class AppointmentForm(forms.ModelForm):
    class Meta:
        model = Appointment
        fields = ['service', 'notes', 'clinic', 'names', 'start_time', 'end_time']
        labels = {'service': 'Service', 'notes': 'Notes', 'clinic': 'Clinic', 'names': 'Name', 'start_time': 'Start time', 'end_time': 'End time'}

class ClinicForm(forms.ModelForm):
    class Meta:
        model = Clinic
        fields = ['dr_name', 'clinic_name', 'location', 'dr_email', 'dr_phonenumber', 'payment_method_available']
        labels = {'dr_name': 'Name', 'clinic_name': 'Clinic Name', 'location': 'Location', 'dr_email': 'Your email', 'dr_phonenumber': 'Your phone number', 'payment_method_available': 'Payment Method for clinic'}