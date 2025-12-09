from flask import Flask, render_template
import requests
from post import Post

app = Flask(__name__)

json = requests.get("https://api.npoint.io/c790b4d5cab58020d391").json()
posts = [Post(p["id"] ,p["title"], p["subtitle"], p["body"]) for p in json]
@app.route("/")
def home():
    return render_template("index.html", posts=posts)

@app.route("/posts/<int:post_id>")
def get_post(post_id):
    post = None
    for p in posts:
        if p.id == post_id:
            post = p
            break

    return render_template("post.html", post=post)

if __name__ == "__main__":
    app.run(debug=True)
