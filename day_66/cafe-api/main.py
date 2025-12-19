from flask import Flask, render_template, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String, Boolean
from random import randint

app = Flask(__name__)


class Base(DeclarativeBase):
    pass


app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///cafes.db'
db = SQLAlchemy(model_class=Base)
db.init_app(app)


class Cafe(db.Model):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String(250), unique=True, nullable=False)
    map_url: Mapped[str] = mapped_column(String(500), nullable=False)
    img_url: Mapped[str] = mapped_column(String(500), nullable=False)
    location: Mapped[str] = mapped_column(String(250), nullable=False)
    seats: Mapped[str] = mapped_column(String(250), nullable=False)
    has_toilet: Mapped[bool] = mapped_column(Boolean, nullable=False)
    has_wifi: Mapped[bool] = mapped_column(Boolean, nullable=False)
    has_sockets: Mapped[bool] = mapped_column(Boolean, nullable=False)
    can_take_calls: Mapped[bool] = mapped_column(Boolean, nullable=False)
    coffee_price: Mapped[str] = mapped_column(String(250), nullable=True)

    def to_dict(self):
        result = {}
        for column in self.__table__.columns:
            result[column.name] = str(getattr(self, column.name))

        return result


with app.app_context():
    db.create_all()


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/random")
def get_random():
    count = db.session.query(Cafe).count()

    random_cafe = db.session.execute(db.select(Cafe).where(Cafe.id == randint(1, count))).scalar()

    return {"cafe": random_cafe.to_dict()}, 200


@app.route("/all")
def get_all():
    all_cafes = db.session.execute(db.select(Cafe)).scalars()

    all_cafes_dict = [cafe.to_dict() for cafe in all_cafes]

    return {"cafes": all_cafes_dict}, 200


@app.route("/search")
def get_by_location():
    cafes_scalars = db.session.execute(db.select(Cafe).where(Cafe.location == request.args.get("loc"))).scalars()
    cafes = [cafe.to_dict() for cafe in cafes_scalars]
    if cafes:
        return {"cafes": cafes}, 200

    return {"error": {"Not Found": "Sorry, we don't have a cafe at that location."}}, 404


@app.route("/add", methods=["POST"])
def add():
    cafe = Cafe(
        name=request.form["name"],
        map_url=request.form["map_url"],
        img_url=request.form["img_url"],
        location=request.form["location"],
        seats=request.form["seats"],
        has_toilet=bool(request.form["has_toilet"]),
        has_wifi=bool(request.form["has_wifi"]),
        has_sockets=bool(request.form["has_sockets"]),
        can_take_calls=bool(request.form["can_take_calls"]),
        coffee_price=bool(request.form["coffee_price"]),
    )

    db.session.add(cafe)
    db.session.commit()

    return jsonify({"response": {"success": "Successfully added the new cafe."}}), 201


@app.route("/update-price/<cafe_id>", methods=["PATCH"])
def update_price(cafe_id):
    cafe = db.session.get(Cafe, cafe_id)

    if cafe:
        cafe.price = request.args.get("new_price")

        db.session.commit()

        return {"success": "Successfully updated the price."}, 200

    return {"error": {"Not Found": "Sorry, a cafe with that id was not found in the database."}}, 404


@app.route("/report-closed/<cafe_id>", methods=["DELETE"])
def delete_cafe(cafe_id):

    if request.args.get("api_key") != "TopSecretAPIKey":

        return {"error": {"Forbidden": "Sorry, that's not allowed, make sure you have the correct api_key."}}, 403

    cafe = db.session.get(Cafe, cafe_id)

    if cafe:
        db.session.delete(cafe)
        db.session.commit()

        return {"success": f"Successfully deleted cafe with id {cafe_id} from the database"}, 200

    return {"error": {"Not Found": "Sorry, a cafe with that id was not found in the database"}}, 404


if __name__ == '__main__':
    app.run(debug=True)
