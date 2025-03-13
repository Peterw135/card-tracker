from db import db

class Card(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(100), nullable = False)
    set_name = db.Column(db.String(100), nullable = False)
    condition = db.Column(db.String(100), nullable = False)
    quantity = db.Column(db.Integer, nullable = False)
    bought_price = db.Column(db.Numeric(10, 2), nullable = False)
    current_price = db.Column(db.Numeric(10, 2))