from django.shortcuts import render, redirect
from .models import Clothing
from .forms import ClothingForm

import requests
import json
# Create your views here.

def located():
    address = requests.get('http://freegeoip.net/json/')
    location = json.loads(address.text)
    return location['city']


def index(request):
    closet = Clothing.objects.all()
    return render(request, 'clothes/index.html', {'closet' : closet})

def add(request):
    if request.method == 'POST':
        form = ClothingForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = ClothingForm()
    return render(request, 'clothes/add.html', {'form' : form})
