# Devices-Price-Classification-System-


**Device Price Prediction API**
This Flask application serves as an API for predicting prices of electronic devices based on their specifications using a trained Support Vector Machine (SVM) model.

**Setup Instructions**
1. Clone Repository: Clone this repository to your local machine.
2. Install Dependencies: Make sure you have Python installed. Install Flask and other required packages using pip install -r requirements.txt
3. Run the Application: Navigate to the project directory and run the following command to start the Flask server:
python app.py
4. Database migrations
how to use Flask-Migrate to manage database migrations:

5. Access the API: Once the server is running, you can access the API endpoints described below.

**API Endpoints**

POST /api/devices: Add a new device to the database with its specifications.
Request Body: JSON object with device specifications (battery_power, px_height, px_width, ram).
Response: JSON object with the ID of the added device.
GET /api/devices/<device_id>: Retrieve the details of a specific device by its ID.
Response: JSON object with device details including predicted price.
GET /api/devices: Retrieve details of all devices in the database.
Response: JSON array of device objects with their details.
POST /api/predict/<device_id>: Predict the price of a device based on its specifications.
Response: JSON object with the predicted price and device ID.

**Database**
The application uses SQLite as its database. The database file devices.db is created automatically in the project directory.


**Trained Model**
The trained SVM model for predicting device prices is loaded from the file svm_model.pkl during application startup.


1. flask db init
