import streamlit as st

def get_weather_of_city(city_name = "Jerusalem"):
  import json
  import requests
  api_key = 'f55667cb75dd795d3f2454dabce5a616'
  base_url = "http://api.openweathermap.org/data/2.5/weather?"
  url = f"{base_url}q={city_name}&appid={api_key}&units=metric"
  response = requests.get(url)
  # print(response)
  weather_json= response.json()
  # print(weather_json)
  formatted_json = json.dumps(weather_json, indent=2)
  # print(formatted_json)
  return weather_json

def preprint_temperature_of_city(city_name = "Jerusalem"):
  weather_json = get_weather_of_city(city_name)
  temperature = weather_json['main']['temp']
  return f"Temperature in {city_name}: {temperature} Celsius"
  # st.write(f"Temperature in {city_name}: {temperature} Celsius")
  # print(f"Temperature in {city_name}: {temperature} Celsius")

def preprint_weather_of_city(city_name = "Jerusalem"):
  weather_json = get_weather_of_city(city_name)

  weather_data = {
    'Temperature': [weather_json['main']['temp']],
    'Feels like': [weather_json['main']['feels_like']],
    'Temp min': [weather_json['main']['temp_min']],
    'Temp max': [weather_json['main']['temp_max']],
    'Humidity': [weather_json['main']['humidity']],
    'Wind speed': [weather_json['wind']['speed']]
  }


  return weather_data

def get_date_time(location_timezone_str='Asia/Jerusalem'):
  import datetime as dt
  import pytz
  import tzlocal
  now = dt.datetime.now()
  utc_tz = pytz.timezone('UTC')
  location_tz = pytz.timezone(location_timezone_str)
  utc_time = utc_tz.localize(now)
  location_time = utc_time.astimezone(location_tz)
  return location_time.strftime('%d.%m.%Y %H:%M')

def preprint_date_time(location_timezone_str = 'Asia/Jerusalem', location_str = 'Jerusalem'):
  return f"Date and time in ***{location_str}***: {get_date_time(location_timezone_str)}"
  # st.write(f"Date and time in {location_str}: {get_date_time(location_timezone_str)}")
  # print(f"Date and time in {location_str}: {get_date_time(location_timezone_str)}")


# Function to get key by value
def get_key(val, options_dict):
    for key, value in options_dict.items():
        if val == value:
            return key
    return "Key not found"




