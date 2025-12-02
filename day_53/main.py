import os

import dotenv
import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from selenium.webdriver.support.expected_conditions import *
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager

dotenv.load_dotenv()

PROPERTY_RESEARCH_DOCS_URL = os.getenv("PROPERTY_RESEARCH_DOCS_URL")
URL = "https://appbrewery.github.io/Zillow-Clone/"

response = requests.get(URL)


def fill_data(inputs, property_info):
    address_input = inputs[0].find_element(By.CLASS_NAME, "whsOnd.zHQkBf")
    price_input = inputs[1].find_element(By.CLASS_NAME, "whsOnd.zHQkBf")
    link_input = inputs[2].find_element(By.CLASS_NAME, "whsOnd.zHQkBf")
    address_input.send_keys(property_info["address"])
    price_input.send_keys(property_info["price"])
    link_input.send_keys(property_info["link"])


def add_property(property_info):
    inputs_list = wait.until(visibility_of_all_elements_located((By.CLASS_NAME, "Qr7Oae")))
    fill_data(inputs_list, property_info)

    send_button = wait.until(element_to_be_clickable((By.CLASS_NAME, "uArJ5e.UQuaGc.Y5sE8d.VkkpIf.QvWxOd")))
    send_button.click()


def extract_data(list_item):
    link = list_item.find("a", class_="StyledPropertyCardDataArea-anchor").get("href")
    price_element = item.find("span", class_="PropertyCardWrapper__StyledPriceLine")
    price = re.search("\\$[\\d]+,?[\\d]+", price_element.get_text()).group()
    address = " ".join(item.find("address").get_text().replace("|", "").strip().split())
    return {
        "address": address,
        "price": price,
        "link": link,
    }


soup = BeautifulSoup(response.content, "html.parser")

items = soup.find_all("li", class_="ListItem-c11n-8-84-3-StyledListCardWrapper")

properties = []
for item in items:
    properties.append(extract_data(item))

if len(properties) > 0:
    options = webdriver.ChromeOptions()
    options.add_experimental_option("detach", True)
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=options)

    driver.get(PROPERTY_RESEARCH_DOCS_URL)

    wait = WebDriverWait(driver, 2)

    for item in properties:
        add_property(item)
        add_another = wait.until(element_to_be_clickable((By.CSS_SELECTOR, "div.c2gzEf a")))
        add_another.click()

    driver.quit()
