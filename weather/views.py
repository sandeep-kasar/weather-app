from django.shortcuts import render
import requests
from weather.models import City
from weather.forms import CityForm


def index(request):
    weather_data = []

    if request.method == 'POST':
        form = CityForm(request.POST)
        form.save()

    form = CityForm()

    url = 'http://api.openweathermap.org/data/2.5/weather?q={}&units=imperial&appid=a14d0bd26203b59e70b6d289617c5fc3'

    cities = City.objects.order_by('-id')

    for city in cities:
        city_weather = requests.get(url.format(city.name)).json()

        weather = {
            'city': city.name,
            'temperature': city_weather['main']['temp'],
            'description': city_weather['weather'][0]['description'],
            'icon': city_weather['weather'][0]['icon']
        }

        weather_data.append(weather)

    context = {"weather_data": weather_data, "form": form}

    return render(request, "weather/index.html", context)
