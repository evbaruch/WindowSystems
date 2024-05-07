import pathlib
import textwrap
import PIL.Image



import google.generativeai as genai

from IPython.display import display
from IPython.display import Markdown

import requests
import json
from google.cloud.aiplatform_v1beta1 import PredictionServiceClient
from datetime import datetime

import os

def to_markdown(text):
  text = text.replace('•', '  *')
  return Markdown(textwrap.indent(text, '> ', predicate=lambda _: True))


#use `os.getenv('GOOGLE_API_KEY')` to fetch an environment variable.
GOOGLE_API_KEY = os.getenv('AIzaSyCzMMBrUrwqxYF-rEvV0989iYUW7uVn0d8')

genai.configure(api_key=GOOGLE_API_KEY)


model = genai.GenerativeModel('gemini-pro-vision')

# Your API key from LocationIQ
LocationIQ_api_key = "pk.dd2f67b1df55bf5c08d2e43cdd7419d9"

# Your API key from OpenWeatherMap
openweathermap_api_key = "df21d91a75fffd8fdbac469d792d0e69"

# Specify the address
address = "Immanuel, Israel"

# URL for the LocationIQ geocoding API
url = f"https://us1.locationiq.com/v1/search.php?key={LocationIQ_api_key}&q={address}&format=json"

# Send a GET request to the API
response = requests.get(url)

# Parse the response as JSON
data = response.json()

# Get the latitude and longitude from the first result
lat = data[0]['lat']
lon = data[0]['lon']

print(f"Latitude: {lat}, Longitude: {lon}")

# URL for the OpenWeatherMap forecast API
url = f"http://api.openweathermap.org/data/2.5/forecast?lat={lat}&lon={lon}&appid={openweathermap_api_key}"

# Send a GET request to the API
response = requests.get(url)

# Parse the response as JSON
data = response.json()

# Get the forecast for the current date
forecast_date = datetime.now().date()

# Placeholder forecast text
forecast_text = f"Weather forecast for {address} on {forecast_date}: Temperature: 20°C, Weather: Clear sky"
# for forecast in data['list']:
#   forecast_date = datetime.fromtimestamp(forecast['dt']).date()
#   if forecast_date == forecast_date:
#     forecast_text = f"Weather forecast for {address} on {forecast_date}: Temperature: {forecast['main']['temp']}K, Weather: {forecast['weather'][0]['description']}"
#     break

zoom = 10

# Construct the URL for the static map image
map_url = f"https://static-maps.yandex.ru/1.x/?l=map&ll={lon},{lat}&z={zoom}&size=650,450&lang=en_US"

# Send a GET request to the URL
map_response = requests.get(map_url)

# Check if the request was successful
if map_response.status_code == 200:
  # Save the map image
  with open('map.png', 'wb') as file:
    file.write(map_response.content)
else:
  print("Error: Unable to retrieve map")
  
img = PIL.Image.open('map.png')
response = model.generate_content(img, stream=True)
response.resolve()
to_markdown(response.text)
