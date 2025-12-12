from flask import Flask, render_template
import requests

app = Flask(__name__)

IMAGES_LOCATION = "static/assets/img/"


@app.route("/")
def get_home():
    posts = requests.get("https://api.npoint.io/68cb1acf64b7e79aa819")
    posts = posts.json()

    return render_template("index.html",
                           title="Gosho's Blog",
                           subtitle="A collections of Gosho's stuff.",
                           header_image="https://images.unsplash.com/photo-1470092306007-055b6797ca72?ixlib=rb-1.2.1&auto=format&fit=crop&w=668&q=80",
                           posts=posts)


@app.route("/about")
def get_about():
    return render_template("about.html",
                           title="About Me",
                           subtitle="This is what I do.",
                           header_image=f"{IMAGES_LOCATION}about-bg.jpg")


@app.route("/contact")
def get_contact():
    return render_template("contact.html",
                           title="Contact Me",
                           subtitle="Have questions? I have answers.",
                           header_image=f"{IMAGES_LOCATION}contact-bg.jpg")


@app.route("/posts/<int:post_id>")
def get_post(post_id):
    posts = requests.get("https://api.npoint.io/68cb1acf64b7e79aa819")
    posts = posts.json()
    post = None
    for p in posts:
        if p["id"] == post_id:
            post = p
            break

    return render_template("post.html",
                           title=post["title"],
                           subtitle=post["subtitle"],
                           header_image=post["image_url"],
                           post=post)


if __name__ == "__main__":
    app.run(debug=True)
