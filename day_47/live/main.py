import os
import smtplib

import dotenv
from selenium import webdriver
from selenium.webdriver.common.by import By

dotenv.load_dotenv()
SENDER = os.getenv("GMAIL")
SENDER_PASSWORD = os.getenv("PASSWORD")
RECEIVER = os.getenv("RECEIVER")
CONNECTION = os.getenv("CONNECTION_SMTP")
ITEM_URL = "https://www.amazon.com/dp/B075CYMYK6?th=1"

TARGET_PRICE = 100

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options)
driver.get(ITEM_URL)

def get_price():
    element = driver.find_element(By.CSS_SELECTOR, "#corePrice_feature_div .a-offscreen")
    return float(element.text.split(" ")[0][1::])


def send_notification(msg):
    global SENDER
    global SENDER_PASSWORD
    global RECEIVER
    global CONNECTION
    global ITEM_URL
    with smtplib.SMTP(CONNECTION, port=587) as connection:
        connection.starttls()
        connection.login(SENDER, SENDER_PASSWORD)
        connection.sendmail(msg=msg, from_addr=SENDER, to_addrs=RECEIVER)


def get_product_title():
    element = driver.find_element(By.ID, "productTitle")
    return element.get_property("textContent")


current_price = get_price()
title = "".join([text.strip() for text in get_product_title().splitlines()])

if current_price < TARGET_PRICE:
    product_title = get_product_title()
    driver.quit()
    message = f"Subject:Amazon Price Alert!\n\n{title} is now ${current_price}\n{ITEM_URL}".encode("UTF-8")
    send_notification(message)
