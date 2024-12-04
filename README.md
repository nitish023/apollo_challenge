# Vehicle API
The Vehicle API is a CRUD-style web service that manages a database of vehicles. This API allows users to create, read, update, and delete vehicle records stored in a database. 

## Setup
- Install dependencies: pip install -r requirements.txt
- Configure the database: Update the database credentials in app.py
- Start the application: python app.py
- Access the API: The API will be available locally at http://127.0.0.1:5000.

## Endpoints
- 'GET /vehicle'
    - Description: Retrieves all vehicle records
    - Response
- 'POST /vehicle'
- 'GET /vehicle/<vin>'
- 'PUT /vehicle/<vin>'
- 'DELETE /vehicle/<vin>'
