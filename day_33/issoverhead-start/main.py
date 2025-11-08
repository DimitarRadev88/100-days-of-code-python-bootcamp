import datetime
import os
import time
from datetime import timedelta

import dotenv
import requests

import email_sender

dotenv.load_dotenv()

my_latitude = float(os.environ.get("LATITUDE"))
my_longitude = float(os.environ.get("LONGITUDE"))
timezone = os.environ.get("TIMEZONE")

parameters = {
    "lat": my_latitude,
    "lng": my_longitude,
    "formatted": 0,
    "tzid": timezone
}


def check_if_iss_is_above():
    iss_location_response = requests.get("http://api.open-notify.org/iss-now.json")
    iss_location_response.raise_for_status()

    current_position = iss_location_response.json()["iss_position"]

    is_at_my_latitude = 5 - my_latitude <= float(current_position["latitude"]) <= 5 + my_latitude
    is_at_my_longitude = 5 - my_longitude <= float(current_position["longitude"]) <= 5 + my_latitude

    return is_at_my_latitude and is_at_my_longitude


def check_if_currently_is_day() -> bool:
    response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()

    results = response.json()["results"]
    sunrise = results["sunrise"]
    sunset = results["sunset"]

    sunrise_hour = int(sunrise.split("T")[1][:2])
    sunset_hour = int(sunset.split("T")[1][:2])
    current_hour = int(str(datetime.timezone(timedelta(hours=9))).split("+")[1][:2])
    is_day = sunrise_hour <= current_hour <= sunset_hour
    return is_day


while True:
    time.sleep(60)

    if check_if_iss_is_above and check_if_currently_is_day():
        sender = email_sender.EmailSender()
        sender.send_email()
