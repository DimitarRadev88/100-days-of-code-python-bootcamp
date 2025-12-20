from flask import Flask, render_template, redirect, url_for
from flask_bootstrap import Bootstrap5
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String, Text
from flask_ckeditor import CKEditor
from datetime import date
from post_form import PostForm

app = Flask(__name__)
app.config["SECRET_KEY"] = "8BYkEfBA6O6donzWlSihBXox7C0sKR6b"
bootstrap = Bootstrap5(app)
ckeditor = CKEditor(app)


class Base(DeclarativeBase):
    pass


app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///posts.db"
db = SQLAlchemy(model_class=Base)
db.init_app(app)


class BlogPost(db.Model):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    title: Mapped[str] = mapped_column(String(250), unique=True, nullable=False)
    subtitle: Mapped[str] = mapped_column(String(250), nullable=False)
    date: Mapped[str] = mapped_column(String(250), nullable=False)
    body: Mapped[str] = mapped_column(Text, nullable=False)
    author: Mapped[str] = mapped_column(String(250), nullable=False)
    img_url: Mapped[str] = mapped_column(String(250), nullable=False)

    def update(self, **kwargs):
        for key, value in kwargs.items():
            setattr(self, key, value)


with app.app_context():
    db.create_all()


@app.route("/")
def get_all_posts():
    posts = db.session.execute(db.select(BlogPost)).scalars().all()

    return render_template("index.html", all_posts=posts)


@app.route("/post/<post_id>")
def show_post(post_id):
    requested_post = db.session.get(BlogPost, post_id)
    return render_template("post.html", post=requested_post)


@app.route("/new-post", methods=["GET", "POST"])
def create_post():
    form = PostForm()

    if form.validate_on_submit():
        new_post = BlogPost(
            title=form.data["title"],
            subtitle=form.data["subtitle"],
            date=date.today().strftime("%B %d, %Y"),
            body=form.data["body"],
            author=form.data["author"],
            img_url=form.data["img_url"]
        )

        db.session.add(new_post)
        db.session.commit()

        return redirect(url_for("get_all_posts"))

    return render_template("make-post.html", form=form)


@app.route("/edit-post/<post_id>", methods=["GET", "POST"])
def edit_post(post_id):
    post = db.session.get(BlogPost, post_id)

    form = PostForm(
        title=post.title,
        subtitle=post.subtitle,
        author=post.author,
        img_url=post.img_url,
        body=post.body
    )

    if form.validate_on_submit():
        post.update(
            title=form.data["title"],
            subtitle=form.data["subtitle"],
            date=date.today().strftime("%B %d, %Y"),
            body=form.data["body"],
            author=form.data["author"],
            img_url=form.data["img_url"]
        )

        db.session.commit()

        return redirect(url_for("show_post", post_id=post.id))

    return render_template("make-post.html", form=form, editing=True)


@app.route("/delete/<post_id>")
def delete_post(post_id):
    post = db.session.get(BlogPost, post_id)
    if post:
        db.session.delete(post)
        db.session.commit()

    return redirect(url_for("get_all_posts"))


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/contact")
def contact():
    return render_template("contact.html")


if __name__ == "__main__":
    app.run(debug=True, port=5003)
