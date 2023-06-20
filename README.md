# crud_appln

# Item Management System

This is an Item Management System that allows users to add, edit, view and delete items. 

## Features

- Add new items with name, description, and price.
- Display a list of existing items with details.
- Edit and delete functionality for each item.
- Client-side form validation.
- Pagination controls and indicators.
- Sorting options for items.
- Proper error handling with meaningful error messages.

## Technologies Used


- Backend API (built with Django and Django REST Framework)

## Getting Started

To get started with the Item Management System, follow these steps:

1. Clone the repository:

   ```shell
   git clone https://github.com/sinan-clt/crud_appln.git

2. Set up the backend:

Navigate to the backend directory:

- Install the Python dependencies:
  pip install -r requirements.txt
  
- Apply the database migrations:
  python manage.py makemigrations
  python manage.py migrate
  
- Add .env file before running which sould contains the database details:
  eg:  
        NAME = 'db_name'
        DB_USER_ACCOUNT = 'db_user'
        PASSWORD = 'db_password'
        HOST = 'db_host'
        PORT = 'db_port'
  
- Run the development server:
  python manage.py runserver
