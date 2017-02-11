from django.shortcuts import render

import requests
import json
# Create your views here.

def located():
    address = requests.get('http://freegeoip.net/json/')
    location = json.loads(address.text)
    return location['city']


def index(request):
    location = located()
    return render(request, 'clothes/index.html', {'location' : location})
