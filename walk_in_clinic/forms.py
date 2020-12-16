from django import forms

from .models import Appointment

class AppointmentForm(forms.ModelForm):
    class Meta:
        model = Appointment
        fields = ['service', 'notes', 'clinic', 'names', 'start_time', 'end_time']
        labels = {'service': 'Service', 'notes': 'Notes', 'clinic': 'Clinic', 'names': 'Name', 'start_time': 'Start time', 'end_time': 'End time'}