from django.shortcuts import render, redirect
from .models import Appointment, Clinic
from .forms import AppointmentForm, ClinicForm
from django.contrib.auth.decorators import login_required, user_passes_test
from django.http import Http404

def index(request):
    """The home page for walk-in-clinic."""
    return render(request, 'walk_in_clinic/index.html')


@login_required
@user_passes_test(lambda u: u.groups.filter(name='Doctors').exists())
def appointments_dr(request):
    """Show all appointments."""
    appointments = Appointment.objects.all().order_by('start_time')
    context = {'appointments': appointments}
    return render(request, 'walk_in_clinic/appointments.html', context)


@login_required
@user_passes_test(lambda u: u.groups.filter(name='Patients').exists())
def appointments(request):
    """Show all appointments."""
    appointments = Appointment.objects.filter(names=request.user).order_by('start_time')
    context = {'appointments': appointments}
    return render(request, 'walk_in_clinic/appointments.html', context)


@login_required
@user_passes_test(lambda u: u.groups.filter(name='Patients').exists())
def appointment(request, appointment_id):
    """Show a single topic"""
    appointment = Appointment.objects.get(id=appointment_id)
    if appointment.names != request.user:
        raise Http404
    context = {'appointment': appointment}
    return render(request, 'walk_in_clinic/appointment.html', context)


@login_required
@user_passes_test(lambda u: u.groups.filter(name='Doctors').exists())
def appointment_dr(request, appointment_id):
    """Show a single topic for dr"""
    appointment = Appointment.objects.get(id=appointment_id)
    context = {'appointment': appointment}
    return render(request, 'walk_in_clinic/appointment_dr.html', context)


@login_required
@user_passes_test(lambda u: u.groups.filter(name='Patients').exists())
def new_appointment(request):
    """Add a new appointment."""
    if request.method != 'POST':
        form = AppointmentForm()
    else:
        form = AppointmentForm(data=request.POST)
        if form.is_valid():
            new_appointment = form.save(commit=False)
            new_appointment.names = request.user
            new_appointment.save()
            return redirect('walk_in_clinic:appointments')

    context = {'form': form}
    return render(request, 'walk_in_clinic/new_appointment.html', context)


@login_required
#@user_passes_test(lambda u: u.groups.filter(name='Patients').exists())
def edit_appointment(request, appointment_id):
    """edit a appointment."""
    appointment = Appointment.objects.get(id=appointment_id)
    if request.method != 'POST':
        form = AppointmentForm(instance=appointment)
    else:
        form = AppointmentForm(instance=appointment, data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('walk_in_clinic:appointment', appointment_id=appointment.id)

    context = {'appointment': appointment, 'form': form}
    return render(request, 'walk_in_clinic/edit_appointment.html', context)


@login_required
@user_passes_test(lambda u: u.groups.filter(name='Doctors').exists())
def new_clinic(request):
    """Add a new appointment."""
    if request.method != 'POST':
        form = ClinicForm()
    else:
        form = ClinicForm(data=request.POST)
        if form.is_valid():
            new_clinic = form.save(commit=False)
            new_clinic.dr_name = request.user
            new_clinic.save()
            return redirect('walk_in_clinic:index')

    context = {'form': form}
    return render(request, 'walk_in_clinic/new_clinic.html', context)


@login_required
@user_passes_test(lambda u: u.groups.filter(name='Patients').exists())
def clinics(request):
    """Show all appointments."""
    clinics = Clinic.objects.all().order_by('clinic_name')
    context = {'clinics': clinics}
    return render(request, 'walk_in_clinic/clinics.html', context)


@login_required
@user_passes_test(lambda u: u.groups.filter(name='Doctors').exists())
def clinics_dr(request):
    clinics = Clinic.objects.filter(dr_name=request.user).order_by('clinic_name')
    context = {'clinics': clinics}
    return render(request, 'walk_in_clinic/clinics.html', context)


@login_required
def clinic(request, clinic_id):
    """Show a individual clinic."""
    clinic = Clinic.objects.get(id=clinic_id)
    context = {'clinic': clinic}
    return render(request, 'walk_in_clinic/clinic.html', context)


@login_required
@user_passes_test(lambda u: u.groups.filter(name='Doctors').exists())
def edit_clinic(request, clinic_id):
    """edit a clinic."""
    clinic = Clinic.objects.get(id=clinic_id)
    if request.method != 'POST':
        form = ClinicForm(instance=clinic)
    else:
        form = ClinicForm(instance=clinic, data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('walk_in_clinic:clinic', clinic_id=clinic.id)

    context = {'clinic': clinic, 'form': form}
    return render(request, 'walk_in_clinic/edit_clinic.html', context)
