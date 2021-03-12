"""
Reginald Long
CS4308 - Internet Programming
Assignment 3 Part 3:
Weather Map
"""

from urllib import request
import json
import datetime

zip_code = 30144
country_code = "US"
user_id = input("Enter your user ID: ")
user_apiid = input("Enter your user apiID: ")
weather_data = request.urlopen(f"https://api.openweathermap.org/data/2.5/weather?&units=Imperial&zip={zip_code},{country_code}&appid={user_apiid}")
data = json.load(weather_data)

print("""
Name:\t{}
Current Temperature:\t{} degrees Fahrenheit
Atmospheric Pressure:\t{} hPa
Wind Speed:\t{} mph
Wind Direction:\t{}
Time of Report:\t{}""".format(
                                data['name'],
                                data['main']['temp'],
                                data['main']['pressure'],
                                data['wind']['speed'],
                                data['wind']['deg'],
                                datetime.datetime.fromtimestamp(data['dt']).strftime('%c'))
                            )