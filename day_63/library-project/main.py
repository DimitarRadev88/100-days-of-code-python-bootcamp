from flask import Flask, render_template, redirect, url_for
from flask_bootstrap import Bootstrap5
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import String, Float, Integer
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column

from book_form import BookForm
from edit_rating_form import EditRatingForm


class Base(DeclarativeBase):
    pass


app = Flask(__name__)
app.config["SECRET_KEY"] = "TopSecretKey"
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///books.db"
bootstrap = Bootstrap5(app)
db = SQLAlchemy(model_class=Base)
db.init_app(app)


class Book(Base):
    __tablename__ = "books"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    title: Mapped[str] = mapped_column(String(250), nullable=False, unique=True)
    author: Mapped[str] = mapped_column(String(250), nullable=False)
    rating: Mapped[int] = mapped_column(Float, nullable=False)


with app.app_context():
    db.create_all()


@app.route('/')
def home():
    books = list(db.session.execute(db.select(Book).order_by(Book.title)).scalars())
    return render_template("index.html", books=books)


@app.route("/add", methods=["GET", "POST"])
def add():
    form = BookForm()
    if form.validate_on_submit():
        book = Book(
            title=form.title.data,
            author=form.author.data,
            rating=form.rating.data
        )
        db.session.add(book)
        db.session.commit()
        return redirect(url_for("home"))

    return render_template("add.html", form=form)


@app.route("/editRating/<int:book_id>", methods=["GET", "POST"])
def edit_rating(book_id):
    form = EditRatingForm()
    book = db.session.execute(db.select(Book).where(Book.id == book_id)).scalar()
    if form.validate_on_submit():
        book.rating = form.rating.data
        db.session.commit()
        return redirect(url_for("home"))

    return render_template("edit.html", form=form, book=book)


@app.route("/deleteBook/<int:book_id>")
def delete_book(book_id):
    book = db.session.execute(db.select(Book).where(Book.id == book_id)).scalar()
    # book = db.get_or_404(Book, book_id)
    db.session.delete(book)
    db.session.commit()

    return redirect(url_for("home"))


if __name__ == "__main__":
    app.run(debug=True)
