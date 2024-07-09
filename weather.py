from dotenv import load_dotenv
from pprint import pprint
import requests
import os

load_dotenv() #loads env vaibles in this case only API_KEY

API_KEY = os.getenv('API_KEY')

def get_current_weather(city="Kingston"):
    request_url = f'https://api.openweathermap.org/data/2.5/weather?appid={API_KEY}&q={city}&units=metric'

    weather_data = requests.get(request_url).json()

    return weather_data

if __name__ == "__main__": # if the program ran from this file directly
    print("\n***Get Current Weather Conditions***\n")

    city = input('Please Enter a city Name: ')
    
    # check empty strings or str with spaces only
    if not bool(city.strip()):
        city = 'Kingston'
    
    weather_data = get_current_weather(city)

    print('\n')
    pprint(weather_data)