from PIL import Image
import requests
from io import BytesIO
import json
import tkinter as tk

def get_weather():
    # make API request for current weather data
    api_key = "afe3e0e9770c14ebcaf48e841cacf4e1"
    city = city_entry.get()
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}"
    url_img = f"https://img.freepik.com/premium-photo/white-cloud-blue-sky_1203-11307.jpg"
    response = requests.get(url)
    weather_data = json.loads(response.text)
    # fetch the image from the URL
    response_img = requests.get(url_img)
    img = Image.open(BytesIO(response_img.content))
    
    # extract temperature in Celsius
    if 'main' in weather_data:
        temp_kelvin = weather_data['main']['temp']
        temp_celsius = temp_kelvin - 273.15
        w_description = weather_data['weather'][0]['description']
        pressure = weather_data['main']['pressure']
        wind_speed = weather_data['wind']['speed']
        output_text.delete(1.0, tk.END)  # clear previous output
        output_text.insert(tk.END, f"Temperature in {city}: {temp_celsius:.2f}°C\n")
        output_text.insert(tk.END, f"{w_description}\n")
        output_text.insert(tk.END, f"Pressure is: {pressure} hPa\n")
        output_text.insert(tk.END, f"Wind Speed is: {wind_speed} m/s\n")
        
    else:
        output_text.delete(1.0, tk.END)  # clear previous output
        output_text.insert(tk.END, "Error: Could not get weather data.\n")



# create window
root = tk.Tk()
root.geometry("400x300")

# create background image
#bg_image = tk.PhotoImage(file="img")


# create canvas and display background image
'''canvas = tk.Canvas(root, width=400, height=300)
canvas.pack(fill="both", expand=True)
canvas.create_image(0, 0, image=img, anchor="center")'''

# create label and entry for city name
city_label = tk.Label(root, text="Enter city name:", font=("Helvetica", 14))
city_label.pack()
city_entry = tk.Entry(root, font=("Helvetica", 14))
city_entry.pack()

# create button to get weather data
get_weather_button = tk.Button(root, text="Get Weather", command=get_weather, font=("Helvetica", 14))
get_weather_button.pack()

# create Text widget to display output data
output_text = tk.Text(root)
output_text.pack()

# start event loop
root.mainloop()
