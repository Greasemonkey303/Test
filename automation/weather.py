#! /bin/python3

import requests

API_KEY = "7debd279d1b46a5cd21136ab45e66873"
BACE_URL = "http://api.openweathermap.org/data/2.5/weather"

city = input("Enter a city name: ")
requests_url = f"{BACE_URL}?appid={API_KEY}&q={city}"
response = requests.get(requests_url)

if response.status_code == 200:
    data = response.json()
    weather = data['weather'][0]['description']
    print(weather)
    temperature = round((data["main"]["temp"] - 273.15) * 9/5 + 32, 2)

    print("Weather:", weather)
    print("Temperature", temperature, "F")


else:
    print("An error occurred.")
