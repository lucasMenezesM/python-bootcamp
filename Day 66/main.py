from flask import Flask, jsonify, render_template, request
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String, Boolean
import random
import os

basedir = os.path.abspath(os.path.dirname(__file__))
database_path = os.path.join(basedir, 'Day 66', 'cafes.db')

app = Flask(__name__)

# CREATE DB
class Base(DeclarativeBase):
    pass
# Connect to Database
# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///cafes.db'
app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{database_path}'

db = SQLAlchemy(model_class=Base)
db.init_app(app)


# Cafe TABLE Configuration
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
        return {column.name: getattr(self, column.name) for column in self.__table__.columns}


with app.app_context():
    db.create_all()


@app.route("/")
def home():
    return render_template("index.html")


# HTTP GET - Read Record

@app.route("/random")
def get_random_cafe():
    cafes = db.session.execute(db.select(Cafe)).scalars().all()
    random_cafe = random.choice(cafes)
    cafe_item = {
        "id": random_cafe.id,
        "name": random_cafe.name,
        "map_url": random_cafe.map_url,
        "img_url": random_cafe.img_url,
        "location": random_cafe.location,
        "seats": random_cafe.seats,
        "has_toilet": random_cafe.has_toilet,
        "has_wifi": random_cafe.has_wifi,
        "has_sockets": random_cafe.has_sockets,
        "can_take_calls": random_cafe.can_take_calls,
        "coffee_price": random_cafe.coffee_price
    }
    result = {"Cafe": cafe_item}
    return jsonify(result)

@app.route("/all")
def get_all_cafes():
    coffees = db.session.execute(db.select(Cafe)).scalars().all()
    coffees_json = [
        {
            "id": coffee.id,
            "name": coffee.name,
            "map_url": coffee.map_url,
            "img_url": coffee.img_url,
            "location": coffee.location,
            "seats": coffee.seats,
            "has_toilet": coffee.has_toilet,
            "has_wifi": coffee.has_wifi,
            "has_sockets": coffee.has_sockets,
            "can_take_calls": coffee.can_take_calls,
            "coffee_price": coffee.coffee_price
        } for coffee in coffees
    ]

    return jsonify(results=coffees_json)


@app.route("/search")
def search_coffee():
    location = request.args.get('location').title()
    cafes = db.session.execute(db.select(Cafe).filter_by(location=location)).scalars().all()
    if len(cafes) > 0:
        results = [cafe.to_dict() for cafe in cafes]
        return jsonify(results=results)
    else:
        return jsonify(error="It was not found any cafe at this location"), 404

# HTTP POST - Create Record

@app.route("/cafe", methods=["POST"])
def create_cafe():
    cafe_item = Cafe(
        name=request.form["name"],
        map_url=request.form["map_url"],
        img_url=request.form["img_url"],
        location=request.form["location"],
        seats=request.form["seats"],
        has_toilet=bool(request.form["has_toilet"]),
        has_wifi=bool(request.form["has_wifi"]),
        has_sockets=bool(request.form["has_sockets"]),
        can_take_calls=bool(request.form["can_take_calls"]),
        coffee_price=request.form["coffee_price"]
    )
    db.session.add(cafe_item)
    db.session.commit()
    return jsonify(response={"Success": "Successfully added new cafe."})

# HTTP PUT/PATCH - Update Record

@app.route("/update-price/<int:cafe_id>", methods=["PATCH"])
def update_cafe_price(cafe_id):
    cafe = db.session.get(Cafe, cafe_id)
    if cafe:
        new_price = request.form["coffee_price"]
        cafe.coffee_price = f"R$ {new_price}"
        db.session.commit()
        return jsonify(response={"Success": "The coffee price was successfully updated!"})
    else:
        return jsonify(response={"Error": "The provided ID was not found"}), 404


# HTTP DELETE - Delete Record

@app.route("/delete/<int:cafe_id>", methods=["DELETE"])
def delete_cafe(cafe_id):
    cafe = db.session.get(Cafe, cafe_id)
    api_key = request.args.get('api_key')
    if cafe:
        if api_key == "TopSecretApiKey":
            db.session.delete(cafe)
            db.session.commit()
            return jsonify(response={"Success": "The cafe was successfully deleted from the database"}), 202
        else:
            return jsonify(response={"Error": "You need to provide a valid api key to complete this action."}), 401
    else:
        return jsonify(response={"Error": "The provided ID was not found."}), 404

if __name__ == '__main__':
    app.run(debug=True)
