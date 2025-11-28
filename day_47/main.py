import os
import smtplib

import dotenv
import requests
from bs4 import BeautifulSoup

dotenv.load_dotenv()
SENDER = os.getenv("GMAIL")
SENDER_PASSWORD = os.getenv("PASSWORD")
RECEIVER = os.getenv("RECEIVER")
CONNECTION = os.getenv("CONNECTION_SMTP")
ITEM_URL = "https://appbrewery.github.io/instant_pot/"
HEADERS = {
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
    "Accept-Encoding": "gzip, deflate, br, zstd",
    "Accept-Language": "en-US,en;q=0.5",
    "Priority": "u=0, i",
    "Sec-Fetch-Dest": "document",
    "Sec-Fetch-Mode": "navigate",
    "Sec-Fetch-Site": "cross-site",
    "Sec-Fetch-User": "?1",
    "Upgrade-Insecure-Requests": "1",
    "User-Agent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:145.0) Gecko/20100101 Firefox/145.0",
}
TARGET_PRICE = 100

response = requests.get(ITEM_URL, headers=HEADERS)

soup = BeautifulSoup(response.content, "html.parser")


def get_price():
    price_element = soup.select_one("div#corePrice_feature_div span.a-offscreen")
    return float(price_element.get_text().split(" ")[0][1::])


def send_notification(message):
    global SENDER
    global SENDER_PASSWORD
    global RECEIVER
    global CONNECTION
    global ITEM_URL
    with smtplib.SMTP(CONNECTION, port=587) as connection:
        connection.starttls()
        connection.login(SENDER, SENDER_PASSWORD)
        connection.sendmail(msg=message, from_addr=SENDER, to_addrs=RECEIVER)


def get_product_title():
    soup = BeautifulSoup(response.content, "html.parser")
    title_element = soup.find("span", id="productTitle")
    return title_element.get_text()


current_price = get_price()
title = "".join([text.strip() for text in get_product_title().splitlines()])

if current_price < TARGET_PRICE:
    product_title = get_product_title()
    message = f"Subject:Amazon Price Alert!\n\n{title} is now ${current_price}\n{ITEM_URL}".encode("UTF-8")
    send_notification(message)
