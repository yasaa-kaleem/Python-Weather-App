from get_location_api import get_location_response
from weather_api import get_weather_response

user_input_zip = input("What is the Zip Code?: ")

location_dict = get_location_response(user_input_zip)

lat = location_dict['lat']
lon = location_dict['lon']

weather_dict = get_weather_response(lat, lon)
forecast = weather_dict['weather'][0]['main']
temp = weather_dict['main']['temp']
city = weather_dict['name']

print(f"In {city}, temp is {temp} and forecast is {forecast}")