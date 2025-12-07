from random import randint

from flask import Flask

app = Flask(__name__)
random_number = randint(0, 9)


@app.route("/")
def home():
    return f"{create_heading("Guess a number between 0 and 9", "black")}" \
           "<img src=https://media.giphy.com/media/3o7aCSPqXE5C6T8tBC/giphy.gif>"


@app.route("/<int:number>")
def guess(number):
    if number < random_number:
        heading = create_heading("Too low, try again!", "red")
        gif_url = "https://media.giphy.com/media/jD4DwBtqPXRXa/giphy.gif"
    elif number > random_number:
        heading = create_heading("Too high, try again!", "purple")
        gif_url = "https://media.giphy.com/media/jD4DwBtqPXRXa/giphy.gif"
    else:
        heading = create_heading("You found me!", "green")
        gif_url = "https://media.giphy.com/media/4T7e4DmcrP9du/giphy.gif"

    return f"{heading}" \
           f"<img src={gif_url}>"

def create_heading(text, color):
    return f"<h1 style='color:{color};'>{text}</h1>"


if __name__ == "__main__":
    app.run(debug=True)
