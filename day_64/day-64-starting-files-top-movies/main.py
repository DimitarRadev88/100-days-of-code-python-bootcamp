from flask import Flask, render_template, redirect, url_for
from flask_bootstrap import Bootstrap5
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String, Float
from rate_movie_form import RateMovieForm
from add_movie_form import AddMovieForm
import requests
import os
import dotenv


app = Flask(__name__)
app.config["SECRET_KEY"] = "8BYkEfBA6O6donzWlSihBXox7C0sKR6b"
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///movies.db"
dotenv.load_dotenv()
OMDB_API_URL = "https://www.omdbapi.com/"
OMDB_API_KEY = os.getenv("OMDB_API_KEY")

Bootstrap5(app)



class Base(DeclarativeBase):
    pass


db = SQLAlchemy(model_class=Base)
db.init_app(app)


class Movie(db.Model):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    title: Mapped[str] = mapped_column(String(250), unique=True, nullable=False)
    year: Mapped[int] = mapped_column(Integer, nullable=False)
    description: Mapped[str] = mapped_column(String(1000), nullable=False)
    rating: Mapped[float] = mapped_column(Float, nullable=True)
    ranking: Mapped[int] = mapped_column(Integer, nullable=True)
    review: Mapped[str] = mapped_column(String(1000), nullable=True)
    img_url: Mapped[str] = mapped_column(String(250), nullable=False)


with app.app_context():
    db.create_all()


# new_movie = Movie(
#     title="Phone Booth",
#     year=2002,
#     description="Publicist Stuart Shepard finds himself trapped in a phone booth, pinned down by an extortionist's sniper rifle. Unable to leave or receive outside help, Stuart's negotiation with the caller leads to a jaw-dropping climax.",
#     rating=7.3,
#     ranking=10,
#     review="My favourite character was the caller.",
#     img_url="https://image.tmdb.org/t/p/w500/tjrX2oWRCM3Tvarz38zlZM7Uc10.jpg"
# )
#
# second_movie = Movie(
#     title="Avatar The Way of Water",
#     year=2022,
#     description="Set more than a decade after the events of the first film, learn the story of the Sully family (Jake, Neytiri, and their kids), the trouble that follows them, the lengths they go to keep each other safe, the battles they fight to stay alive, and the tragedies they endure.",
#     rating=7.3,
#     ranking=9,
#     review="I liked the water.",
#     img_url="https://image.tmdb.org/t/p/w500/t6HIqrRAclMCA60NsSmeqe9RmNV.jpg"
# )


# with app.app_context():
#     db.session.bulk_save_objects([new_movie, second_movie])
#     db.session.commit()


@app.route("/")
def home():
    movies = list(db.session.execute(db.select(Movie).order_by(Movie.rating.asc())).scalars())
    count = len(movies)
    for n in range(0, count):
        movies[n].ranking = count - n

    return render_template("index.html", movies=movies)


@app.route("/edit/<movie_id>", methods=["GET", "POST"])
def edit(movie_id):
    movie = db.session.execute(db.select(Movie).where(Movie.id == movie_id)).scalar()
    form = RateMovieForm()

    if form.validate_on_submit():
        movie.rating = form.rating.data
        movie.review = form.review.data

        db.session.commit()

        return redirect(url_for("home"))

    return render_template("edit.html", movie=movie, form=form)


@app.route("/delete/<movie_id>")
def delete(movie_id):
    movie = db.session.execute(db.select(Movie).where(Movie.id == movie_id)).scalar()

    db.session.delete(movie)
    db.session.commit()

    return redirect(url_for("home"))


@app.route("/add", methods=["GET", "POST"])
def add():
    form = AddMovieForm()

    if form.validate_on_submit():
        params = {
            "apikey": OMDB_API_KEY,
            "t": form.title.data
        }
        movie_data = requests.get(OMDB_API_URL, params=params).json()

        movie = Movie(
            title=movie_data["Title"],
            year=movie_data["Year"],
            description=movie_data["Plot"],
            img_url=movie_data["Poster"]
        )

        db.session.add(movie)
        db.session.commit()

        saved = db.session.execute(db.select(Movie).where(Movie.title == movie.title)).scalar()

        return redirect(url_for("edit", movie_id=saved.id))

    return render_template("add.html", form=form)


if __name__ == "__main__":
    app.run()
