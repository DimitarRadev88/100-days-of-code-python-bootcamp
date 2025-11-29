from selenium import webdriver
from selenium.webdriver.common.by import By

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options)

driver.get("https://en.wikipedia.org/wiki/Main_Page")

element = driver.find_element(By.CSS_SELECTOR, "#articlecount ul > li:nth-child(2) a")

print(element.text)

driver.quit()
