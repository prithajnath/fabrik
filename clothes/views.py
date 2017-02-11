from django.shortcuts import render
from .models import Clothing

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
    return render(request, 'clothes/add.html')
