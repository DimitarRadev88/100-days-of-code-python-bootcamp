# import sqlite3
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String, Float

app = Flask(__name__)


# db = sqlite3.connect("some-data.db")
# cursor = db.cursor()
# cursor.execute("CREATE TABLE books (id INTEGER PRIMARY_KEY, title VARCHAR(250) NOT NULL UNIQUE, author VARCHAR(250) NOT NULL, rating FLOAT NOT NULL)")
# cursor.execute("INSERT INTO books VALUES(1, 'Harry Potter', 'J.K.Rowling', '9.3')")
# db.commit()

class Base(DeclarativeBase):
    pass


app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///new-books-collection.db"
db = SQLAlchemy(model_class=Base)
db.init_app(app)


class Book(db.Model):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    title: Mapped[str] = mapped_column(String(250), unique=True, nullable=False)
    author: Mapped[str] = mapped_column(String(250), nullable=False)
    rating: Mapped[float] = mapped_column(Float, nullable=False)


def print_all_books_titles():
    with app.app_context():
        books = db.session.execute(db.select(Book).order_by(Book.title)).scalars()
        for b in books:
            print(b.title)


with app.app_context():
    db.create_all()

with app.app_context():
    book = Book(
        title="Harry Potter",
        author="J. K. Rowling",
        rating=9.3
    )
    db.session.add(book)
    db.session.commit()

print_all_books_titles()

with app.app_context():
    result = db.session.execute(db.select(Book).where(Book.title == "Harry Potter")).scalar()
    print(result.title)

with app.app_context():
    result = db.session.execute(db.select(Book).where(Book.title == "Harry Potter")).scalar()
    result.title = "Harry Potter and the Goblet of Fire"
    db.session.commit()

print_all_books_titles()

with app.app_context():
    result = db.session.execute(db.select(Book).where(Book.id == 1)).scalar()
    db.session.delete(result)
    db.session.commit()

print_all_books_titles()
