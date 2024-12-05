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

    def as_dict(self):
        return {
            "vin": self.vin,
            "manufacturer_name": self.manufacturer_name,
            "description": self.description,
            "horse_power": self.horse_power,
            "model_name": self.model_name,
            "model_year": self.model_year,
            "purchase_price": float(self.purchase_price),  # Convert Decimal to float
            "fuel_type": self.fuel_type
        }