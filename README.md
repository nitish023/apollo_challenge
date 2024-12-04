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
    - Response:
        - Status Code: 200 OK
        - Body: JSON array of vehicle records 
- 'POST /vehicle'
    - Description: Add a new vehicle record
    - Request: JSON object of vehicle
    - Response:
        - Status Code: 201 Created
        - Body: JSON object of the new vehicle
- 'GET /vehicle/<vin>'
    - Description: Retrieves a specific vehicle by VIN
    - Response: 
        - Status Code: 200 OK (if found)
        - Status Code: 404 Not Found (else)
        - Body: JSON object of the vehicle
- 'PUT /vehicle/<vin>'
    - Description: Update a vehicle record by VIN
    - Response:
        - Status Code: 200 OK (if found)
        - Status Code: 404 Not Found (else)
        - Body: JSON object of the vehicle
- 'DELETE /vehicle/<vin>'
    - Description: Delete a vehicle by VIN
    - Response:
        - Status Code: 204 No Content (if successful)
        - Status Code: 404 Not Found (else)
