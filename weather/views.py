from django.shortcuts import render
from pyowm import OWM
from user.models import Location
from clothes.models import Clothing
import requests
import json
import os

#API_KEY = os.environ.get('OWM')
API_KEY = '13d1090375aba1e54b0051ff825ab553'

# Create your views here.
def index(request):
    """
    Gets the latitude and longitude of the user from the database which they
    provided from the location form. Used the HTML5 geolocation API to find
    their coordinates and saves it into the database. Using the latitude and
    longitude to find the current weather using Open Weather Map's API and their
    weater_at_coords method which takes a latitude and longitude parameter.
    """
    if request.user.is_authenticated():
        current_user = Location.objects.get(user = request.user.id)
        latitude = current_user.latitude
        longitude = current_user.longitude

        owm = OWM(API_KEY)
        observation = owm.weather_at_coords(latitude, longitude)
        w = observation.get_weather()
        current_temperature = w.get_temperature('fahrenheit')
        current_status = w.get_status()
        
        clothes = Clothing.objects.filter(owned_by = request.user.id, clothing_type = current_status)
        
        

        return render(request, 'weather/index.html', {
            'current_temperature' : round(current_temperature['temp']),
            'current_status' : current_status, 'clothes' : clothes
            })
    else:
        return render(request, 'weather/index.html')
