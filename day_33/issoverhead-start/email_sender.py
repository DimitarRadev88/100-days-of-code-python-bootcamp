import smtplib
import dotenv
import os

class EmailSender:

    def __init__(self):
        dotenv.load_dotenv()
        self.email = os.environ.get("GMAIL")
        sender_password = os.environ.get("PASSWORD")
        smtp = os.environ.get("CONNECTION_SMTP")
        self.connection = smtplib.SMTP(smtp)
        self.connection.starttls()
        self.connection.login(self.email, sender_password)


    def send_email(self):
        self.connection.sendmail(self.email, self.email, msg="Subject:Look Up!\n\n The ISS is passing above you!")