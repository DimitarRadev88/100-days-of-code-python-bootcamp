import requests
import dotenv
import os
from twilio.rest import Client

dotenv.load_dotenv()

api_key = os.environ.get("OPEN_WEATHER_API_KEY")
latitude = os.environ.get("LATITUDE")
longitude = os.environ.get("LONGITUDE")

params = {
    "lat": latitude,
    "lon": longitude,
    "appid": api_key,
    "units": "metric",
    "cnt": 4
}

response = requests.get("https://api.openweathermap.org/data/2.5/forecast", params)
response.raise_for_status()

weather_data = response.json()

weather_ids = [data["weather"][0]["id"] for data in weather_data["list"] if data["weather"][0]["id"] < 700]


def send_notification(message):
    account_sid = os.environ.get("TWILIO_ACCOUNT_SID")
    auth_token = os.environ.get("TWILIO_AUTH_TOKEN")
    from_phone_number = os.environ.get("TWILIO_PHONE_NUMBER")
    to_phone_number = os.environ.get("MY_PHONE_NUMBER")
    client = Client(account_sid, auth_token)

    return client.messages.create(
        body=message,
        from_=from_phone_number,
        to=to_phone_number,
    )

if len(weather_ids) > 0:

    notification = send_notification("It's going to rain today. Remember to brin an ☂️")
    print(notification.body)