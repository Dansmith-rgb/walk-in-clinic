from django.shortcuts import render
from .models import Appointment

def index(request):
    """The home page for walk-in-clinic."""
    return render(request, 'walk_in_clinic/index.html')

def appointments(request):
    """Show all appointments."""
    appointments = Appointment.objects.all().order_by('service')
    context = {'appointments': appointments}
    return render(request, 'walk_in_clinic/appointments.html', context)