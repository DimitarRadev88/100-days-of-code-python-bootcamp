import datetime
import os
import smtplib
from random import choice

import dotenv
import pandas


def get_birthday_people():
    data_frame = pandas.read_csv("birthdays_file.csv")
    birthdays_dict = data_frame.to_dict(orient="records")
    today = datetime.datetime.now()
    return [p for p in birthdays_dict if p["month"] == today.month and p["day"] == today.day]


def send_birthday_wish(bd_person):
    letter_names = os.listdir("letter_templates")
    letter_location = "letter_templates/" + choice(letter_names)
    dotenv.load_dotenv()
    sender = os.environ.get("GMAIL")
    password = os.environ.get("PASSWORD")
    smtp = os.environ.get("CONNECTION_SMTP")

    with open(letter_location, mode="r") as letter_file:
        letter = letter_file.read()
        personal_letter = letter.replace("[NAME]", bd_person["name"])

    with smtplib.SMTP(smtp) as connection:
        connection.starttls()
        connection.login(sender, password)
        connection.sendmail(sender, bd_person["email"],
                            msg=f"Subject:Happy Birthday, {bd_person["name"]}!\n\n{personal_letter}")


people_with_birthdays = get_birthday_people()

for person in people_with_birthdays:
    send_birthday_wish(person)
