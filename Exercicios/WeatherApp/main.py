import requests
import json
from pprint import pprint

API_Key = 'ea66cb5a64e820427e4a6514cea63507'
city = str(input('Digite uma cidade: '))
base_url = "http://api.openweathermap.org/data/2.5/weather?appid="+API_Key+"&q="+city

weather_data = requests.get(base_url).json()
pprint(weather_data)
temperatura = weather_data["main"]["temp"]
celsius = temperatura - 273.15

print("A Temperatura atual em {} é de {:.1f}ºC".format(city, celsius))