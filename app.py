from flask import Flask, request, jsonify
import joblib
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate



# Load the trained SVM model
model = joblib.load('/Users/shirinwadood/Desktop/projects/classification/Devices-Price-Classification-System-/svm_classifier.pkl')

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///devices.db'
db = SQLAlchemy(app)



class Device(db.Model):
    __tablename__ = 'device'  
    id = db.Column(db.Integer, primary_key=True)
    battery_power = db.Column(db.Integer)
    px_height = db.Column(db.Integer)
    px_width = db.Column(db.Integer)
    ram = db.Column(db.Integer)
    predictedPrice = db.Column(db.Float)


with app.app_context():
    db.create_all()


@app.route('/api/devices', methods=['POST'])
def add_device():
    try:
        data = request.json
        specs = data['specs']
        device = Device(
            battery_power=specs['battery_power'],
            px_height=specs['px_height'],
            px_width=specs['px_width'],
            ram=specs['ram']
        )

        db.session.add(device)
        db.session.commit()

        return jsonify({'device_id': device.id}), 201
    except Exception as e:
        print(f"Error occurred: {e}")  # Log the error
        return jsonify({'error': str(e)}), 500


@app.route('/api/devices/<int:id>', methods=['GET'])
def get_device(id):
    device = Device.query.get_or_404(id)
    return jsonify({
        'id': device.id,
        'battery_power': device.battery_power,
        'px_height': device.px_height,
        'px_width': device.px_width,
        'ram': device.ram,
        'predictedPrice': device.predictedPrice
    })

@app.route('/api/devices', methods=['GET'])
def get_all_devices():
    devices = Device.query.all()
    device_list = []
    for device in devices:
        device_list.append({
            'id': device.id,
            'battery_power': device.battery_power,
            'px_height': device.px_height,
            'px_width': device.px_width,
            'ram': device.ram,
            'predictedPrice': device.predictedPrice
        })
    return jsonify({'devices': device_list})

@app.route('/api/predict/<int:device_id>', methods=['POST'])
def predict_price(device_id):
    try:
        device = Device.query.get_or_404(device_id)

        # Predict the price
        predicted_price = model.predict([[device.battery_power, device.px_height, device.px_width, device.ram]])[0]

        # Update the device with the predicted price
        device.predictedPrice = predicted_price
        db.session.commit()

        return jsonify({'predicted_price': predicted_price, 'device_id': device.id})
    except Exception as e:
        return jsonify({'error': str(e)})

if __name__ == '__main__':
    app.run(debug=True)
