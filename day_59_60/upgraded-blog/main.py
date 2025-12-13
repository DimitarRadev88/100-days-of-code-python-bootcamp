import requests
from flask import Flask, render_template, request
import smtplib
import dotenv
import os

dotenv.load_dotenv()
SENDER = os.getenv("GMAIL")
PASSWORD = os.getenv("PASSWORD")
CONNECTION_SMTP = os.getenv("CONNECTION_SMTP")

app = Flask(__name__)


@app.route("/")
def get_home():
    posts = requests.get("https://api.npoint.io/68cb1acf64b7e79aa819")
    posts = posts.json()

    return render_template("index.html", posts=posts)


@app.route("/about")
def get_about():
    return render_template("about.html")


@app.route("/contact", methods=["GET", "POST"])
def contact():
    if request.method == "GET":
        return render_template("contact.html", title="Contact Me")
    else:
        data = {
            "name": request.form["name"],
            "email": request.form["email"],
            "phone": request.form["phone"],
            "message": request.form["message"]
        }

        send_email(data)

        return render_template("contact.html", title="Successfully sent your message")


@app.route("/posts/<int:post_id>")
def get_post(post_id):
    posts = requests.get("https://api.npoint.io/68cb1acf64b7e79aa819")
    posts = posts.json()
    post = None
    for p in posts:
        if p["id"] == post_id:
            post = p
            break

    return render_template("post.html", post=post)


def send_email(data):
    connection = smtplib.SMTP(CONNECTION_SMTP)
    connection.starttls()
    connection.login(SENDER, PASSWORD)

    message = f"Subject: Message from {data["name"]}\n\nMessage: {data["message"]}\nPhone: {data["phone"]}\nEmail: {data["email"]}"

    connection.sendmail(from_addr=SENDER, to_addrs=data["email"], msg=message)

    connection.quit()


if __name__ == "__main__":
    app.run(debug=True)
