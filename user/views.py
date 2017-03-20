from django.shortcuts import render
from django.contrib.auth.models import User
from django import forms
from .forms import RegisterForm
from .models import Profile

# Create your views here.

def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            userObj = form.cleaned_data
            username = userObj['username']
            password = userObj['password']
            email = userObj['email']
            fname = userObj['first_name']
            location = userObj['location']
            if not (User.objects.filter(username=username).exists() or User.objects.filter(email=email).exists()):
                User.objects.create_user(username, email, password)
                p = Profile(first_name=fname, location=location )
                p.save()

            else:
                raise forms.ValidationError('Username or email has been taken!')
    else:
        form = RegisterForm()
    return render(request, 'user/register.html', {'form' : form})
