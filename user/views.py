from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.http import HttpResponseRedirect
from django import forms
from .forms import UserForm

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
                return HttpResponseRedirect('/')
        else:
            raise forms.ValidationError('Username or email has been taken already!')
    else:
        user_form = UserForm()

    return render(request, 'user/register.html', {'user_form' : user_form})
