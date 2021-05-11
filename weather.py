import requests, json, os

api_key = os.environ['weatherkey']

base_url = "http://api.openweathermap.org/data/2.5/weather?"


complete_url = base_url + "appid=" + api_key + "&q=" + city_name

