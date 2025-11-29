from selenium import webdriver
from selenium.webdriver.common.by import By

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options)
driver.get("https://www.amazon.com/dp/B075CYMYK6?th=1")
element = driver.find_element(By.CSS_SELECTOR, "#corePrice_feature_div .a-offscreen")
print(element.get_property("textContent"))
driver.quit()