from django.shortcuts import render
from pyowm import OWM
import requests
import json

API_KEY = '13d1090375aba1e54b0051ff825ab553'

# Create your views here.
def index(request):
    address = requests.get('http://freegeoip.net/json/')
    location_json = json.loads(address.text)
    location = location_json['city'] + ',' + location_json['country_code']
    owm = OWM(API_KEY)
    observation = owm.weather_at_place(location)
    w = observation.get_weather()
    current_temperature = w.get_temperature('fahrenheit')
    current_status = w.get_status()
    return render(request, 'weather/index.html', {
        'location' : location,
        'current_temperature' : current_temperature['temp'],
        'current_status' : current_status
        })

"""
from pyowm import OWM

API_KEY = '13d1090375aba1e54b0051ff825ab553'

city = input('Where do you live? ')
owm = OWM(API_KEY)
reg = owm.city_id_registry()
location = reg.ids_for(city, matching='nocase')
city_id = location[0][0]
observation = owm.weather_at_id(city_id)
current_weather = observation.get_weather()
print(current_weather.get_wind())
print(current_weather.get_temperature('fahrenheit'))
"""
