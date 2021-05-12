import requests, json, os

def getTemperature(wx):
  x = wx["main"]
  tempK = x["temp"]
  return (tempK - 273.15) * (9/5) + 32

def getCurrentDescr(wx):
  x = wx["weather"]
  return x[0]["description"]

def getCurrentBasic(wx):
  x = wx["weather"]
  return x[0]["main"]

def getData(city):
  api_key = os.environ['weatherkey']
  base_url = "http://api.openweathermap.org/data/2.5/weather?"
  complete_url = base_url + "appid=" + api_key + "&q=" + city
  response = requests.get(complete_url)
  wx = response.json()
  return wx

