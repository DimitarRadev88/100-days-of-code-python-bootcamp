from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

from day_51.speed_test_bot import SpeedTestBot

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=options)

speed_test_bot = SpeedTestBot(driver)

speeds = speed_test_bot.get_current_speeds()

print(speeds)
