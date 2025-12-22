from datetime import date
from flask import Flask, render_template, redirect, url_for, flash
from flask_bootstrap import Bootstrap5
from flask_ckeditor import CKEditor
from flask_login import login_user, LoginManager, current_user, logout_user, login_required
from functools import wraps
from werkzeug.security import generate_password_hash, check_password_hash

from forms import CreatePostForm, UserRegisterForm, UserLoginForm, CommentForm
from blog_db import database, BlogPost, User, Comment, SQLALCHEMY_DATABASE_URI

app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
ckeditor = CKEditor(app)
Bootstrap5(app)

login_manager = LoginManager()
login_manager.init_app(app)


app.config['SQLALCHEMY_DATABASE_URI'] = SQLALCHEMY_DATABASE_URI
database.init_app(app)

with app.app_context():
    # database.drop_all()
    database.create_all()


def admin_only(func):
    @wraps(func)
    def decorated_view(*args, **kwargs):
        if not current_user.is_authenticated or int(current_user.id) != 1:
            return login_manager.unauthorized()
        return func(*args, **kwargs)

    return decorated_view


@login_manager.user_loader
def user_loader(user_id):
    logged_user = database.session.get(User, int(user_id))
    return logged_user


@login_manager.unauthorized_handler
def unauthorized_handler():
    flash("You don't have access to this feature")
    return redirect(url_for("login"))

@app.route('/register', methods=["GET", "POST"])
def register():
    form = UserRegisterForm()
    if form.validate_on_submit():
        if database.session.execute(database.select(User).where(User.email == form.data.get("email"))).scalar():
            flash("You've already signed up with that email, log in instead.")
            return redirect(url_for("register"))

        user = User(
            name=form.data.get("name"),
            email=form.data.get("email"),
            password=generate_password_hash(form.data.get("password"), salt_length=8)
        )

        database.session.add(user)
        database.session.commit()

        return redirect(url_for("login"))

    return render_template("register.html", form=form)


@app.route('/login', methods=["GET", "POST"])
def login():
    form = UserLoginForm()
    if form.validate_on_submit():
        user = database.session.execute(database.select(User).where(User.email == form.data.get("email"))).scalar()
        if not user:
            flash("That email does not exist, please try again.")
            return redirect(url_for("login"))
        if not check_password_hash(user.password, form.data.get("password")):
            flash("Wrong password!")
            return redirect(url_for("login"))

        login_user(user)
        return redirect(url_for("get_all_posts"))

    return render_template("login.html", form=form)


@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('get_all_posts'))


@app.route('/')
def get_all_posts():
    result = database.session.execute(database.select(BlogPost))
    posts = result.scalars().all()
    return render_template("index.html", all_posts=posts)


@app.route("/post/<int:post_id>")
def show_post(post_id):
    form = CommentForm()
    requested_post = database.get_or_404(BlogPost, post_id)
    return render_template("post.html", post=requested_post, form=form)


@app.route("/new-post", methods=["GET", "POST"])
@admin_only
def add_new_post():
    form = CreatePostForm()
    if form.validate_on_submit():
        new_post = BlogPost(
            title=form.title.data,
            subtitle=form.subtitle.data,
            body=form.body.data,
            img_url=form.img_url.data,
            date=date.today().strftime("%B %d, %Y"),
            user_id=current_user.id
        )
        database.session.add(new_post)
        database.session.commit()
        return redirect(url_for("get_all_posts"))
    return render_template("make-post.html", form=form)


@app.route("/edit-post/<int:post_id>", methods=["GET", "POST"])
@admin_only
def edit_post(post_id):
    post = database.get_or_404(BlogPost, post_id)
    edit_form = CreatePostForm(
        title=post.title,
        subtitle=post.subtitle,
        img_url=post.img_url,
        body=post.body
    )

    if edit_form.validate_on_submit():
        post.title = edit_form.title.data
        post.subtitle = edit_form.subtitle.data
        post.img_url = edit_form.img_url.data
        post.body = edit_form.body.data
        database.session.commit()
        return redirect(url_for("show_post", post_id=post.id))
    return render_template("make-post.html", form=edit_form, is_edit=True)


@app.route("/delete/<int:post_id>")
@admin_only
def delete_post(post_id):
    post_to_delete = database.get_or_404(BlogPost, post_id)
    database.session.delete(post_to_delete)
    database.session.commit()
    return redirect(url_for('get_all_posts'))


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/contact")
def contact():
    return render_template("contact.html")


@app.route("/comment/<int:post_id>", methods=["POST"])
@login_required
def leave_comment(post_id):
    form = CommentForm()
    if form.validate_on_submit():
        blog_post = database.session.get(BlogPost, post_id)
        comment = Comment(
            text=form.data.get("text"),
            user=current_user,
            blog_post=blog_post
        )

        database.session.add(comment)
        database.session.commit()

    return redirect(url_for("show_post", post_id=post_id))


if __name__ == "__main__":
    app.run(debug=True, port=5002)
