import json
import requests
from pprint import pprint
import os

config_path = os.path.join(os.path.dirname(__file__), 'config.json')

with open(config_path) as config_file:
    config = json.load(config_file)
    API_Key = config['API_Key']


city = str(input('Digite uma cidade: '))
base_url = f"http://api.openweathermap.org/data/2.5/weather?appid={API_Key}&q={city}&units=metric"

weather_data = requests.get(base_url).json()
pprint(weather_data)
temperatura = weather_data["main"]["temp"]
celsius = temperatura - 273.15

print("A Temperatura atual em {} é de {:.1f}ºC".format(city, temperatura))
