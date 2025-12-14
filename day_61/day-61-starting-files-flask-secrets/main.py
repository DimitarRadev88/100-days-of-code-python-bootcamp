from flask import Flask, render_template, redirect, url_for
from flask_bootstrap import Bootstrap5

from login_form import LoginForm

app = Flask(__name__)
app.secret_key = "some secret string"

bootstrap = Bootstrap5(app=app)

EMAIL = "admin@email.com"
PASSWORD = "12345678"


@app.route("/")
def home():
    return render_template('index.html')


@app.route("/login", methods=["GET", "POST"])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.email.data == EMAIL and form.password.data == PASSWORD:
            return redirect(url_for("success"))
        return redirect(url_for("denied"))
    return render_template("login.html", form=form)


@app.route("/denied")
def denied():
    return render_template("denied.html")


@app.route("/success")
def success():
    return render_template("success.html")


if __name__ == '__main__':
    app.run(debug=True)
