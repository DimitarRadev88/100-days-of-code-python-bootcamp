import time

from selenium import webdriver
from selenium.webdriver.common.by import By

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options)

driver.get("https://ozh.github.io/cookieclicker/")

time.sleep(1)

language_selector_en = driver.find_element(By.ID, "langSelect-EN")

language_selector_en.click()

time.sleep(1)


def click_cookie():
    cookie = driver.find_element(By.ID, "bigCookie")
    cycle_end = time.time() + 2
    while time.time() < cycle_end:
        cookie.click()


def buy_product():
    available_products = driver.find_elements(By.CLASS_NAME, "product.unlocked.enabled")
    if len(available_products) > 0:
        available_products[-1].click()


def buy_upgrade():
    available_upgrades = driver.find_elements(By.CLASS_NAME, "crate.upgrade.enabled")
    if len(available_upgrades) > 0:
        available_upgrades[-1].click()


game_end_time = time.time() + 5 * 60

num = 1


def click_golden_cookie():
    golden_cookie = driver.find_element(By.ID, "goldenCookie")
    if golden_cookie.is_displayed():
        print("Golden cookie clicked")


while time.time() < game_end_time:
    click_cookie()
    buy_upgrade()
    time.sleep(0.1)
    buy_product()
    click_golden_cookie()

cookies_per_second_element = driver.find_element(By.ID, "cookiesPerSecond")

print(f"Cookies {cookies_per_second_element.text}")
driver.quit()
