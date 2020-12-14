from django.db import models
from django import forms
from django.core.exceptions import ValidationError



class Appointment(models.Model):
    """A appointment the user creates"""
    service = models.CharField(max_length=200)
    notes = models.CharField(max_length=200, default="No notes at this time")
    clinic = models.ForeignKey('Clinic', on_delete=models.CASCADE, blank=True)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()

    def check_overlap(self, fixed_start, fixed_end, new_start, new_end):
        overlap = False
        if new_start == fixed_end or new_end == fixed_start:    #edge case
            overlap = False
        elif (new_start >= fixed_start and new_start <= fixed_end) or (new_end >= fixed_start and new_end <= fixed_end): #innner limits
            overlap = True
        elif new_start <= fixed_start and new_end >= fixed_end: #outter limits
            overlap = True
 
        return overlap
    
    def clean(self):
        if self.end_time <= self.start_time:
            raise ValidationError('Ending times must after starting times')
 
        appointments = Appointment.objects.filter(start_time=self.start_time)
        if appointments.exists():
            for appointment in appointments:
                if self.check_overlap(appointment.start_time, appointment.end_time, self.start_time, self.end_time):
                    raise ValidationError(
                        'There is an overlap with another appointment: ' + str(
                            appointment.start_time) + ' ' + str(appointment.end_time))

    def __str__(self):
        return self.service

class Clinic(models.Model):
    """A clinic can be set up by Doctor"""
    clinic_name = models.CharField(max_length=50, default=" ")
    location = models.CharField(max_length=50, default="39 York Road, London, SW81 4AQ, England")
    dr_email = models.EmailField(max_length=50, default="Dan")
    dr_phonenumber = models.IntegerField(default=5263648574)
    payment_methods = [
        ('pp', 'PayPal'),
        ('cc', 'Credit Card'),
        ('dc', 'Debit Card'),
        ('ca', 'Cash')
    ]
    payment_method_available = models.CharField(max_length=2,choices=payment_methods,default=payment_methods[1])

    def __str__(self):
        return self.clinic_name