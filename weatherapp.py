import requests
import json

api_key = "afe3e0e9770c14ebcaf48e841cacf4e1"
city = input("Enter city name: ")

# make API request for current weather data
url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}"
response = requests.get(url)
weather_data = json.loads(response.text)

# print the entire dictionary to check for issues
#print(weather_data)

# display current weather data
if 'main' in weather_data:
    print("Current Weather:")
    
    print(f"Temperature in Kelvin: {weather_data['main']['temp']} Kelvin")
    print(f"Weather Description: {weather_data['weather'][0]['description']}")
    temp_kelvin = weather_data['main']['temp']
    temp_celsius = temp_kelvin - 273.15
    print(f"Temperature: {temp_celsius:.2f}°C")
    print(f"Pressure: {weather_data['main']['pressure']} Pa")
    print(f"Humidity: {weather_data['main']['humidity']} %")
    print(f"Wind speed: {weather_data['wind']['speed']} m/s")
    
else:
    print("Error: Could not get weather data.")

