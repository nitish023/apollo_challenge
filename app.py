from flask import Flask, jsonify, request
from models import db, Vehicle

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:Qwerty_105@localhost/apollo'
db.init_app(app)

def validate_vehicle(data):
    required_fields = ['vin', 'manufacturer_name', 'horse_power', 'model_name', 'model_year', 'purchase_price', 'fuel_type']
    errors = {}
    for field in required_fields:
        if field not in data:
            errors[field] = f'{field} is required.'
        elif not data[field]:
            errors[field] = f'{field} cannot be empty.'
    return errors

def get_vehicle_by_vin(vin):
    return Vehicle.query.filter_by(vin=vin.lower()).first()

@app.route('/')
def index():
    return "Apollo Coding Challenge"

@app.route('/vehicle', methods=['GET'])
def get_vehicles():
    vehicles = Vehicle.query.all()
    return jsonify([vehicle.as_dict() for vehicle in vehicles]), 200

@app.route('/vehicle', methods=['POST'])
def create_vehicle():
    try:
        data = request.json
    except Exception:
         return jsonify({'error': 'Invalid JSON'}), 400
    errors = validate_vehicle(data)
    if errors:
        return jsonify({'errors': errors}), 422
    data['vin'] = data['vin'].lower()
    new_vehicle = Vehicle(**data)
    db.session.add(new_vehicle)
    db.session.commit()
    return jsonify(new_vehicle.as_dict()), 201

@app.route('/vehicle/<vin>', methods=['GET'])
def get_vehicle(vin):
    vehicle = get_vehicle_by_vin(vin)
    if not vehicle:
        return jsonify({'error': 'Vehicle not found'}), 404
    return jsonify(vehicle.as_dict()), 200

@app.route('/vehicle/<vin>', methods=['PUT'])
def update_vehicle(vin):
    vehicle = get_vehicle_by_vin(vin)
    if not vehicle:
        return jsonify({'error': 'Vehicle not found'}), 404
    try:
        data = request.json
    except Exception:
        return jsonify({'error': 'Invalid JSON'}), 400
    for key, value in data.items():
        setattr(vehicle, key, value)
    db.session.commit()
    return jsonify(vehicle.as_dict()), 200

@app.route('/vehicle/<vin>', methods=['DELETE'])
def delete_vehicle(vin):
    vehicle = get_vehicle_by_vin(vin)
    if not vehicle:
        return jsonify({'error': 'Vehicle not found'}), 404
    db.session.delete(vehicle)
    db.session.commit()
    return '', 204

@app.errorhandler(400)
def bad_request(e):
    return jsonify({'error': 'Bad Request'}), 400

@app.errorhandler(422)
def unprocessable_entry(e):
    return jsonify(({'error': 'Unprocessable Entry'})), 422

if __name__ == '__main__':
    app.run(debug=True)