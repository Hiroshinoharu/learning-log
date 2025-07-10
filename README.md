# Learning Log

Learning Log is a Django web application that allows users to track their learning progress by creating topics and adding entries under those topics. The app supports user authentication, ensuring that users can only manage their own topics and entries. It uses Django Bootstrap 5 for styling and is deployable on Platform.sh.

## Features

- User registration and authentication
- Create, view, and manage learning topics
- Add, edit, and view entries under each topic
- Secure access to user-specific data
- Responsive UI with Bootstrap 5
- Deployment support for Platform.sh

## Installation

1. Ensure you have Python 3.8 installed.
2. Clone the repository.
3. Create and activate a virtual environment:
   ```bash
   python -m venv env
   source env/bin/activate  # On Windows use `env\Scripts\activate`
   ```
4. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Usage

1. Apply migrations:
   ```bash
   python manage.py migrate
   ```
2. Create a superuser (optional, for admin access):
   ```bash
   python manage.py createsuperuser
   ```
3. Run the development server:
   ```bash
   python manage.py runserver
   ```
4. Access the app at `http://127.0.0.1:8000/`

## Deployment

This project supports deployment on Platform.sh. The configuration files `.platform.app.yaml`, `.platform/routes.yaml`, and `.platform/services.yaml` are included for this purpose.

## Project Structure

- `ll_project/`: Django project configuration
- `learning_logs/`: Main app for managing learning topics and entries
- `accounts/`: User authentication and registration app
- `templates/`: HTML templates for the app
- `requirements.txt`: Python dependencies
- `manage.py`: Django management script

## License

This project does not specify a license.
