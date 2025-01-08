# Bus Inventory Application

This is a simple Django application to manage a Bus Inventory. It allows you to:

1. **View the list of buses** in the inventory.
2. **Add new buses** to the inventory.

## Features
- View all buses with details like bus number, brand, seats, trip, trip duration, conductor, and driver.
- Add a new bus using a simple form.

## Requirements
- Python (>= 3.x)
- Django (>= 4.x)

## Installation Steps
1. Clone the repository:
   ```bash
   git clone <repository-url>
   cd bus-inventory
   ```
2. Create and activate a virtual environment:
   ```bash
   python3 -m venv benv
   source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
   ```
3. Install the required packages:
   ```bash
   pip install -r requirements.txt
   ```
4. Apply the database migrations:
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```
5. Run the development server:
   ```bash
   python manage.py runserver
   ```
6. Open the app in your browser:
   - Visit: `http://127.0.0.1:8000/`

## File Structure
- **models.py**: Defines the `Bus` model for storing bus details.
- **forms.py**: Creates the form to add new buses.
- **views.py**: Contains the logic for listing and adding buses.
- **urls.py**: Maps URLs to the views.
- **templates/**: Contains HTML templates for displaying and adding buses.

## How to Use
1. Go to the homepage to see the list of buses.
2. Click "Add New Bus" to open the form.
3. Fill in the details and submit the form.
4. The new bus will appear in the inventory list.

## Example Bus Details
- **Bus Number**: KA-01-1234
- **Brand**: Volvo
- **No of Seats**: 50
- **Trip**: Bangalore to Hyderabad
- **Trip Duration**: 12:30:00
- **Conductor**: Ravi
- **Driver**: Mohan

## Contribution
Feel free to fork the repository and submit pull requests.

## License
This project is licensed under the MIT License.

