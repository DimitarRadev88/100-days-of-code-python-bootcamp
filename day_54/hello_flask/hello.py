from flask import Flask

app = Flask(__name__)

def make_bold(function):
    def add_tag():
        return "<b>" + function() + "</b>"

    return add_tag

def make_emphasis(function):
    def add_tag():
        return "<em>" + function() + "</em>"

    return add_tag

def make_underlined(function):
    def add_tag():
        return "<u>" + function() + "</u>"

    return add_tag

@app.route("/")
@make_bold
@make_emphasis
@make_underlined
def hello_world():
    return "Hello world"

@app.route("/bye")
def bye():
    return "Bye"

@app.route("/username/<name>")
def greet(name):
    return f"Hello, {name}!"

if __name__ == "__main__":
    app.run(debug=True)