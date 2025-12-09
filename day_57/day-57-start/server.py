import random
from datetime import datetime

import requests
from flask import Flask, render_template

app = Flask(__name__)


def get_age_prediction(name):
    age_response = requests.get(f"https://api.agify.io?name={name}")
    age_content = age_response.json()
    return age_content["age"]


def get_gender_prediction(name):
    gender_response = requests.get(f" https://api.genderize.io?name={name}")
    gender_content = gender_response.json()
    return gender_content["gender"]


@app.route("/")
def home():
    return render_template("index.html",
                           page_heading="Hello world!",
                           random_number=random.randint(0, 100),
                           copyright_year=datetime.now().year)


@app.route("/guess/<name>")
def guess(name):
    age = get_age_prediction(name)
    gender = get_gender_prediction(name)
    return render_template("guess.html", name=name.title(), age=age, gender=gender)

@app.route("/blog")
def get_blog():
    response = requests.get("https://api.npoint.io/c790b4d5cab58020d391")
    posts = response.json()
    return render_template("blog.html", posts=posts)

if __name__ == "__main__":
    app.run(debug=True)
