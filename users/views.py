from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from .forms import UserRegistrationForm
from django.contrib.auth.models import Group

def register(request):
    """Register a new user."""
    if request.method != 'POST':
        form = UserRegistrationForm
    else:
        form = UserRegistrationForm(data=request.POST)

        if form.is_valid():
            new_user = form.save()
            if form.cleaned_data['role'] == "dr":
                my_group = Group.objects.get(name='Doctors') 
                my_group.user_set.add(new_user)
            else:
                my_group = Group.objects.get(name='Patients') 
                my_group.user_set.add(new_user)
            #new_user.save()
            login(request, new_user)
            return redirect('walk_in_clinic:index')

    context = {'form': form}
    return render(request, 'registration/register.html', context)


