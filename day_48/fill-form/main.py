from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import dotenv
import os

dotenv.load_dotenv()

FIRST_NAME = "SELENIUM"
LAST_NAME = "INPUT"
EMAIL_ADDRESS = "some@email.address"

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options)

driver.get("https://secure-retreat-92358.herokuapp.com/")

first_name_input = driver.find_element(By.NAME, "fName")

first_name_input.send_keys(FIRST_NAME, Keys.ENTER, LAST_NAME, Keys.ENTER, EMAIL_ADDRESS, Keys.ENTER)

driver.quit()
