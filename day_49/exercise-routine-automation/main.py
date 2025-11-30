import os
import time

from selenium import webdriver
from selenium.common import TimeoutException
from selenium.webdriver.chrome.service import Service as ChromiumService
from selenium.webdriver.common.by import By
from selenium.webdriver.support.expected_conditions import *
from selenium.webdriver.support.expected_conditions import visibility_of_all_elements_located
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.core.os_manager import ChromeType

HOME_URL = "https://appbrewery.github.io/gym/"
LOGIN_URL = "https://appbrewery.github.io/gym/login/"
USER_DATA_DIR = os.path.join(os.getcwd(), "chrome_profile")
ACCOUNT_NAME = "gym.account"
ACCOUNT_EMAIL = "gym.account@email.com"
ACCOUNT_PASSWORD = "strongpassword123"


def login():
    login_button = wait.until(element_to_be_clickable((By.ID, "login-button")))
    login_button.click()
    email_input = wait.until(visibility_of_element_located((By.ID, "email-input")))
    email_input.clear()
    email_input.send_keys(ACCOUNT_EMAIL)
    password_input = wait.until(visibility_of_element_located((By.ID, "password-input")))
    password_input.clear()
    password_input.send_keys(ACCOUNT_PASSWORD)
    submit_button = wait.until(visibility_of_element_located((By.ID, "submit-button")))
    submit_button.click()
    wait.until(presence_of_element_located((By.ID, "schedule-page")))


def find_classes(day_of_week, time):
    day_schedules = wait.until(visibility_of_all_elements_located((By.CLASS_NAME, "Schedule_dayGroup__y79__")))

    wanted_day_schedule = None

    for schedule in day_schedules:
        if day_of_week in schedule.find_element(By.CLASS_NAME, "Schedule_dayTitle__YBybs").text:
            wanted_day_schedule = schedule

    class_elements = wanted_day_schedule.find_elements(By.CLASS_NAME, "ClassCard_card__KpCx5")

    classes_to_book = []

    for cl in class_elements:
        if f"Time: {time}" in cl.text:
            classes_to_book.append(cl)

    return classes_to_book


summary_dict = {
    "Classes Booked": 0,
    "Waitlists joined": 0,
    "Already booked/waitlisted": 0,
    "Total 6pm classes processed": 0,
}

detailed_info = {
    "[New Booking]": [],
    "[New Waitlist]": [],
    "[Booked]": [],
    "[Waitlisted]": []
}


def book_class(cl):
    book_button = cl.find_element(By.CLASS_NAME, "ClassCard_bookButton__DMM1I")

    if book_button.text == "Booked":
        print(f"Already booked:\n{cl.text}")
        summary_dict["Already booked/waitlisted"] += 1
        summary_dict["Total 6pm classes processed"] += 1
        detailed_info["[Booked]"].append(cl.text)
    elif book_button.text == "Waitlisted":
        print(f"Already waitlisted:\n{cl.text}")
        summary_dict["Already booked/waitlisted"] += 1
        summary_dict["Total 6pm classes processed"] += 1
        detailed_info["[Waitlisted]"].append(cl.text)
    elif book_button.text == "Join Waitlist":
        book_button.click()
        wait.until(
            presence_of_element_located((By.CLASS_NAME, "ClassCard_bookButton__DMM1I.ClassCard_waitlisted__ExoHW")))
        print(cl.text)
        summary_dict["Waitlists joined"] += 1
        summary_dict["Total 6pm classes processed"] += 1
        detailed_info["[New Waitlist]"].append(cl.text)
    else:
        book_button.click()
        wait.until(presence_of_element_located((By.CLASS_NAME, "ClassCard_bookButton__DMM1I.ClassCard_booked__cxTZ1")))
        print(cl.text)
        summary_dict["Classes Booked"] += 1
        summary_dict["Total 6pm classes processed"] += 1
        detailed_info["[New Booking]"].append(cl.text)

    print("\n")


def verity_bookings_titles():
    driver.find_element(By.ID, "my-bookings-link").click()
    bookings_list_titles = wait.until(
        visibility_of_all_elements_located((By.CSS_SELECTOR, ".MyBookings_bookingDetails__QG0l_ h3")))
    for booking in bookings_list_titles:
        print(f"  ✓ Verified: {booking.text}")

    print("--- VERIFICATION RESULT ---")
    expected_count = summary_dict["Total 6pm classes processed"]
    print(f"Expected: {expected_count} bookings")
    actual_count = len(bookings_list_titles)
    print(f"Found: {actual_count} bookings")

    if expected_count != actual_count:
        print(f"❌ MISMATCH: Missing {expected_count - actual_count} bookings")
    else:
        print("✅ SUCCESS: All bookings verified!")


def retry(func, retries=7, description=None, args=None):
    attempts = 1
    while attempts <= 7:
        print(print(f"Trying {description}. Attempt: {attempts}"))
        try:
            if args:
                return func(args)
            return func()
        except TimeoutException:
            time.sleep(1)
            attempts += 1
            if attempts == retries:
                raise


def book_classes():
    classes = find_classes("Tue", "6:00 PM")
    classes.extend(find_classes("Thu", "6:00 PM"))

    for class_ in classes:
        retry(book_class, args=class_)


options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
options.add_argument(f"user-data-dir={USER_DATA_DIR}")

driver = webdriver.Chrome(service=ChromiumService(ChromeDriverManager(chrome_type=ChromeType.CHROMIUM).install()),
                          options=options)
driver.get(HOME_URL)

wait = WebDriverWait(driver, 2)

retry(login, description="login")

book_classes()

print("--- BOOKING SUMMARY ---\n")
for entry in summary_dict:
    print(f"{entry}: {summary_dict[entry]}")

print("\n")

print("--- DETAILED CLASS LIST ---\n")
for entry in detailed_info:
    for li in detailed_info[entry]:
        print(f"  • {entry}:\n{li}\n")

print(f"--- Total Tuesday/Thursday 6pm classes: {summary_dict["Total 6pm classes processed"]} ---")

print("--- VERIFYING ON MY BOOKINGS PAGE ---")

retry(verity_bookings_titles, description="verify bookings")
