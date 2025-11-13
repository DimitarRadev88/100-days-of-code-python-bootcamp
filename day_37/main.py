import datetime
import os

import dotenv
import requests
from aiohttp import ClientError

dotenv.load_dotenv()

PIXELA_ENDPOINT = "https://pixe.la/v1/users"
USERNAME = os.environ.get("PIXELA_USERNAME")
TOKEN = os.environ.get("PIXELA_TOKEN")
GRAPH_ID = os.environ.get("GRAPH_ID")
GRAPH_NAME = os.environ.get("GRAPH_NAME")
GRAPH_UNIT = "kilogram"
GRAPH_TYPE = "float"
GRAPH_COLOR = "ajisai"
AGREE = "yes"

HEADERS = {
    "X-USER-TOKEN": TOKEN
}


def create_account():
    body = {
        "token": TOKEN,
        "username": USERNAME,
        "agreeTermsOfService": AGREE,
        "notMinor": AGREE
    }

    response = requests.post(PIXELA_ENDPOINT, json=body)
    print(response.status_code)


def create_graph():
    body = {
        "id": GRAPH_ID,
        "name": GRAPH_NAME,
        "unit": GRAPH_UNIT,
        "type": GRAPH_TYPE,
        "color": GRAPH_COLOR
    }

    response = requests.post(PIXELA_ENDPOINT + f"/{USERNAME}/graphs", json=body, headers=HEADERS)
    print(response.text)


def get_quantity(date):
    response = requests.get(PIXELA_ENDPOINT + f"/{USERNAME}/graphs/{GRAPH_ID}/{date}", headers=HEADERS)
    response.raise_for_status()
    return float(response.json()["quantity"])


def create_pixel(date):
    body = {
        "date": date,
        "quantity": "0",
    }

    response = requests.post(PIXELA_ENDPOINT + f"/{USERNAME}/graphs/{GRAPH_ID}", json=body, headers=HEADERS)
    print(response.status_code)


def update_pixel(date, quantity):
    try:
        old_quantity = get_quantity(date)
    except ClientError:
        create_pixel(date)
    else:
        quantity = quantity + old_quantity

    body = {
        "quantity": str(quantity)
    }

    response = requests.put(PIXELA_ENDPOINT + f"/{USERNAME}/graphs/{GRAPH_ID}/{date}", json=body, headers=HEADERS)
    print(response.status_code)


pixel_date = datetime.datetime.now().strftime("%Y%m%d")
new_quantity = float(input("Quantity: "))

update_pixel(pixel_date, new_quantity)
