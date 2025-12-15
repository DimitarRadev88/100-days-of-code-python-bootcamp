import csv

import pandas
from flask import Flask, render_template, redirect, url_for
from flask_bootstrap import Bootstrap5

from cafe_form import CafeForm

app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
Bootstrap5(app)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/add", methods=["GET", "POST"])
def add_cafe():
    form = CafeForm()
    if form.validate_on_submit():
        with open("cafe-data.csv", newline="\r\n", encoding="utf-8", mode="a") as csv_file:
            writer = csv.writer(csv_file, delimiter=",")
            writer.writerow([form.cafe_name.data, form.location.data, form.opening_time.data, form.closing_time.data,
                             form.coffee_rating.data, form.wifi_rating.data, form.power_sockets.data])
        return redirect(url_for('add_cafe'))

    return render_template('add.html', form=form)


@app.route("/cafes")
def cafes():
    with open("cafe-data.csv", newline="", encoding="utf-8", mode="r") as csv_file:
        read_csv = pandas.read_csv(csv_file).to_dict("records")
    return render_template("cafes.html", cafes=read_csv)


if __name__ == "__main__":
    app.run(debug=True)
