
import sys
import json
import requests
from twilio.rest import Client

# Gather weather data in farenheit
url = "https://api.openweathermap.org/data/2.5/weather?q=<location>&APPID=<your_api_key>&units=imperial"
r = requests.get(url)
weather_json = r.json()

#Twilio info
account_sid = '<your_twilio_sid>"
auth_token = '<your_twili_auth_token>'

# parse locationa and temp
temp = weather_json['main']['temp']
location = weather_json['name']

# create and send message via sms
client = Client(account_sid, auth_token)

message = client.messages.create(
                                from_ = '<your_twilio_number',
                                body = f"The temperature in {location} right now is {temp}.",
                                to = '<receiving_phone_number'
                            )
                            
# prints the message id to console to confirm success
print(message.sid)
