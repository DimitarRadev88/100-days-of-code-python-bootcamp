import datetime
from datetime import timedelta

import requests

parameters = {
    "lat": 35.433331,
    "lng": 139.649994,
    "formatted": 0,
    "tzid": "Asia/Tokyo"
}

response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
response.raise_for_status()

results = response.json()["results"]
sunrise = results["sunrise"]
print(f"Sunrise at {sunrise}")
sunset = results["sunset"]
print(f"Sunset at {sunset}")

sunrise_hour = sunrise.split("T")[1][:2]
sunset_hour = sunset.split("T")[1][:2]
current_hour = str(datetime.timezone(timedelta(hours=9))).split("+")[1][:2]


print(f"Currently is {"Day" if sunrise_hour < current_hour < sunset_hour else "Night"}")
