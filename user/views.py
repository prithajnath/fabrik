from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.http import HttpResponseRedirect
from django import forms
from .forms import UserForm, LocationForm
from .models import Location

# Create your views here.

def register(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            username = data['username']
            password = data['password']
            email = data['email']
            first_name = data['first_name']
            if not (User.objects.filter(username=username).exists() or User.objects.filter(email=email).exists()):
                x = User.objects.create_user(username = username, password = password, email = email)
                x.first_name = first_name
                x.save()
                user = authenticate(username = username, password = password)
                login(request, user)
                return HttpResponseRedirect('/user/location')
        else:
            raise forms.ValidationError('Username or email has been taken already!')
    else:
        user_form = UserForm()

    return render(request, 'user/register.html', {'user_form' : user_form})

def location(request):
    if request.method == 'POST':
        location_form = LocationForm(request.POST)
        if location_form.is_valid():
            data = location_form.cleaned_data
            latitude = data['latitude']
            longitude = data['longitude']
            '''
            Checks if the user already has a location saved in the database. If
            the user does, then it will update the location row with the current
            values in the form. Otherwise, it will create a new row in the
            database with the values from the form.
            '''
            x = Location.objects.update_or_create(user=request.user, latitude = latitude, longitude = longitude)
            return HttpResponseRedirect('/')
    else:
        location_form = LocationForm()
    return render(request, 'user/location.html', {'location_form' : location_form})

def profile(request):
    user = User.objects.filter(username=request.user.username)
    return render(request, 'user/profile.html', {'user' : user})

def setting(request):
    return render(request, 'user/setting.html')
