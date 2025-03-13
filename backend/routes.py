from flask import Blueprint
from model import Card, db

routes = Blueprint('routes', __name__)

@routes.route("/")
def home():
    return "This is the home page"

@routes.route("/add_card")
def add_card():
    new_card = Card(
        name = "Charizard",
        set_name = "Base Set",
        condition = "Near Mint",
        quantity = 1,
        bought_price = "500"
    )
    db.session.add(new_card)
    db.session.commit()
    return {"message": "Card added successfully"}
