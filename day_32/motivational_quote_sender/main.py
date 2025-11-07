import os
import smtplib
from random import choice
import datetime

import dotenv

weekday = datetime.datetime.now().strftime("%A")

def send_motivational_quote():

    with open("quotes.txt") as quotes_file:
        quotes = quotes_file.readlines()

    msg_quote = choice(quotes)

    dotenv.load_dotenv()

    sender_email = os.environ.get("GMAIL")
    sender_password = os.environ.get("PASSWORD")
    receiver_email = os.environ.get("RECEIVER")
    smtp = os.environ.get("CONNECTION_SMTP")

    with smtplib.SMTP(smtp) as connection:
        connection.starttls()
        connection.login(sender_email, sender_password)
        connection.sendmail(sender_email, receiver_email, f"Subject:Happy {weekday}\n\n{msg_quote}")


if weekday == "Friday":
    send_motivational_quote()