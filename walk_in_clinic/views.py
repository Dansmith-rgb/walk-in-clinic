from django.shortcuts import render, redirect
from .models import Appointment
from .forms import AppointmentForm

def index(request):
    """The home page for walk-in-clinic."""
    return render(request, 'walk_in_clinic/index.html')

def appointments(request):
    """Show all appointments."""
    appointments = Appointment.objects.all().order_by('service')
    context = {'appointments': appointments}
    return render(request, 'walk_in_clinic/appointments.html', context)

def appointment(request, appointment_id):
    """Show a single topic"""
    appointment = Appointment.objects.get(id=appointment_id)
    context = {'appointment': appointment}
    return render(request, 'walk_in_clinic/appointment.html', context)

def new_appointment(request):
    """Add a new appointment."""
    if request.method != 'POST':
        form = AppointmentForm()
    else:
        form = AppointmentForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('walk_in_clinic:appointments')

    context = {'form': form}
    return render(request, 'walk_in_clinic/new_appointment.html', context)