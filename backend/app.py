from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from dotenv import load_dotenv
import os

load_dotenv()

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

class Card(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(100), nullable = False)
    set_name = db.Column(db.String(100), nullable = False)
    condition = db.Column(db.String(100), nullable = False)
    quantity = db.Column(db.Integer, nullable = False)
    bought_price = db.Column(db.Numeric(10, 2), nullable = False)
    current_price = db.Column(db.Numeric(10, 2))

with app.app_context():
    db.create_all()

@app.route("/")
def home():
    return "This is the home page"

@app.route("/add_card")
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

if __name__ == '__main__':
    app.run(debug=True)