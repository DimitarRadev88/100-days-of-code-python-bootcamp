from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.expected_conditions import *
from selenium.webdriver.common.by import By


class SpeedTestBot:

    def __init__(self, web_driver):
        self.url = "https://www.speedtest.net/"
        self.download_speed = 0
        self.upload_speed = 0
        self.driver = web_driver
        self.wait = WebDriverWait(self.driver, 2)

    def __open_test_website(self):
        print(f"Opening {self.url}")
        self.driver.get(self.url)
        reject_button = self.wait.until(element_to_be_clickable((By.ID, "onetrust-reject-all-handler")))
        reject_button.click()

    def __test_speed(self):
        print("Starting test")
        start_test_link = self.wait.until(element_to_be_clickable((By.CLASS_NAME, "js-start-test.test-mode-multi")))
        start_test_link.click()

        while True:
            gauge_wrapper = self.driver.find_element(By.CLASS_NAME, "gauge-wrapper")
            self.driver.implicitly_wait(2)
            if gauge_wrapper.get_attribute("style") == "visibility: hidden;":
                break

        print("Test finished")

        self.driver.implicitly_wait(2)

        self.download_speed = self.wait.until(
            visibility_of_element_located((By.CLASS_NAME, "result-data-large.number.result-data-value.download-speed"))).text
        self.upload_speed = self.wait.until(
            visibility_of_element_located((By.CLASS_NAME, "result-data-large.number.result-data-value.upload-speed"))).text


    def get_current_speeds(self):
        self.__open_test_website()
        self.__test_speed()
        self.driver.quit()
        return {
            "Download speed": self.download_speed,
            "Upload speed": self.upload_speed
        }