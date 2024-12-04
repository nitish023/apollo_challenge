from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Vehicle(db.Model):
    vin = db.Column(db.String(20), primary_key=True)
    manufacturer_name = db.Column(db.String(255), nullable=False)
    description = db.Column(db.Text)
    horse_power = db.Column(db.Integer, nullable=False)
    model_name = db.Column(db.String(255), nullable=False)
    model_year = db.Column(db.Integer, nullable=False)
    purchase_price = db.Column(db.Numeric(10, 2), nullable=False)
    fuel_type = db.Column(db.String(50), nullable=False)