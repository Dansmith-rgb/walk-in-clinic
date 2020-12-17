from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class UserRegistrationForm(UserCreationForm):
    email = forms.EmailField()
    role_choices = [
        ('pa', 'Patient'),
        ('dr', 'Doctor')
    ]
    role = forms.ChoiceField(choices=role_choices)

    class Meta:
        model = User
        fields = ['username', 'email', 'role', 'password1', 'password2']