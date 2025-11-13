import datetime
import os

import dotenv
import requests
from twilio.rest import Client

dotenv.load_dotenv()

ALPHA_VANTAGE_API_KEY = os.environ.get("ALPHA_VANTAGE_API_KEY")
NEWS_API_KEY = os.environ.get("NEWS_API_KEY")
TWILIO_ACCOUNT_SID = os.environ.get("TWILIO_ACCOUNT_SID")
TWILIO_AUTH_TOKEN = os.environ.get("TWILIO_AUTH_TOKEN")
TWILIO_PHONE_NUMBER = os.environ.get("TWILIO_PHONE_NUMBER")
MY_PHONE_NUMBER = os.environ.get("MY_PHONE_NUMBER")
STOCK_NAME = "ORCL"
COMPANY_NAME = "Oracle Corporation"
STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"


def get_stock_percent_difference():
    yesterday_date = datetime.date.today() - datetime.timedelta(days=1)
    day_before_yesterday_date = yesterday_date - datetime.timedelta(days=1)

    params = {
        "function": "TIME_SERIES_DAILY",
        "symbol": STOCK_NAME,
        "apikey": ALPHA_VANTAGE_API_KEY,
        "outputsize": "compact"
    }

    response = requests.get(f"{STOCK_ENDPOINT}", params)
    response.raise_for_status()

    stock_data = response.json()["Time Series (Daily)"]

    day_before_yesterday_stock_closing_price = float(stock_data[str(day_before_yesterday_date)]["4. close"])

    yesterday_stock_closing_price = float(stock_data[str(yesterday_date)]["4. close"])

    percent_difference = (1 - day_before_yesterday_stock_closing_price / yesterday_stock_closing_price) * 100

    return percent_difference


def get_news():
    params = {
        "apiKey": NEWS_API_KEY,
        "q": COMPANY_NAME,
        "pageSize": 3
    }

    response = requests.get(f"{NEWS_ENDPOINT}", params)
    response.raise_for_status()

    return {f"Headline: {article["title"]}": f"Brief: {article["description"]}" for article in
            response.json()["articles"]}


def send_notification(message):
    client = Client(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)
    message = client.messages.create(body=message, from_=TWILIO_PHONE_NUMBER, to=MY_PHONE_NUMBER)
    print(message.body)


difference = get_stock_percent_difference()

if abs(difference) > 1:
    company_news = get_news()
    for (title, description) in company_news.items():
        sign = "🔻" if difference < 0 else "🔺"
        notification_message = f"{STOCK_NAME}: {sign}{abs(round(difference))}%\n{title}\n{description}"
        notification_message = notification_message[:147] + "..." if len(
            notification_message) > 150 else notification_message

        send_notification(notification_message)
