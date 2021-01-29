import requests
import os
from twilio.rest import Client

api_key = os.environ.get("OWM_API_KEY")
OWM_Endpoint = "https://api.openweathermap.org/data/2.5/onecall"
account_sid = "AC22afa3db868a9c64e70cc2598a6ff70e"
auth_token = os.environ.get("AUTH_TOKEN")

parameter = {
    "lat": 40.387878,
    "lon": -111.849167,
    "appid": api_key,
    "exclude": "current,minutely,daily"
}

response = requests.get(OWM_Endpoint, params=parameter)
response.raise_for_status()
weather_data = response.json()
weather_slice = weather_data["hourly"][:12]

will_rain = False
for hour in weather_slice:
    condition_code = hour["weather"][0]["id"]
    if int(condition_code) < 800:
        will_rain = True

if will_rain:
    print("Bring an umbrella.")
    client = Client(account_sid, auth_token)
    message = client.messages \
        .create(
           body="Bring an umbrella.☂",
           from_="+13174837336",
           to='+13852399946'
        )
    print(message.status)
