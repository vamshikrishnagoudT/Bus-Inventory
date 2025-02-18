# Bus-Inventory
## Overview
This Django-based web application manages bus information, allowing users to view, add, delete, and update bus records. It also includes API endpoints for interacting with the bus data programmatically.

## Features
- View a list of buses
- Add a new bus
- Delete an existing bus
- Fetch buses with less than 31 seats (API)
- Update bus data via API

## Installation
### Prerequisites
- Python 3.x
- Django
- Django REST Framework

### Setup
1. Clone the repository:
   ```sh
   git clone <repository-url>
   cd <repository-folder>
   ```

2. Create and activate a virtual environment:
   ```sh
   python -m venv env
   source env/bin/activate  # On Windows use `env\Scripts\activate`
   ```

3. Install dependencies:
   ```sh
   pip install -r requirements.txt
   ```

4. Apply database migrations:
   ```sh
   python manage.py migrate
   ```

5. Start the development server:
   ```sh
   python manage.py runserver
   ```

## Usage
### Web Interface
- Navigate to `http://127.0.0.1:8000/` to see the list of buses.
- Use the "Add Bus" form to add a new bus.
- Click on delete to remove a bus entry.

### API Endpoints
#### Fetch all buses (JSON)
```http
GET /api/bus-list/
```
#### Fetch buses with less than 31 seats
```http
GET /api/buses/less-than-31-seats/
```
#### Update bus data
```http
PUT /api/update-bus/
Content-Type: application/json
Body: {
  "data": [
    {
      "id": 1,
      "bus_number": "123A",
      "brand": "Volvo",
      "no_of_seats": 30,
      "trip": "City Center",
      "trip_duration": "02:30:00",
      "conductor": "John Doe",
      "driver": "Jane Smith"
    }
  ]
}
```

## Technologies Used
- Django
- Django REST Framework
- SQLite (Default Database)
- HTML/CSS (Frontend Templates)

## License
This project is licensed under the MIT License.


