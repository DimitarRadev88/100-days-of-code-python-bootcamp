from selenium import webdriver
from selenium.webdriver.common.by import By

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options)

driver.get("https://www.python.org/")

element = driver.find_element(By.CLASS_NAME, "medium-widget.event-widget.last")

items = element.find_elements(By.TAG_NAME, "li")

event_dict = {}

for n in range(0, len(items)):
    time = items[n].find_element(By.TAG_NAME, "time")
    event = items[n].find_element(By.TAG_NAME, "a")
    event_dict[n] = {
        time.text: event.text
    }

driver.quit()

print(event_dict)