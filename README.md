# Event Registration System

The Event Registration System is a web application built with Django that allows users to view, register for, and manage events. It provides features for event creation, registration, and reporting.

## Features

- User registration and authentication
- Event creation and management (for superusers/admins)
- Event registration and unregistration
- Viewing registered events
- Reporting features for users and events

## Installation

1. Clone the repository:

```bash
git clone https://github.com/joshgervais/joshgervais-256A03.git
``````

2. Navigate to the project directory:

```bash
cd event-registration
``````

3. Apply database migrations:

```bash
python manage.py migrate
``````

4. Create a superuser account:

```bash
python manage.py createsuperuser
``````

5. Start the development server:

```bash
python manage.py runserver
``````

6. Access the application in your web browser at `http://localhost:8000`.

## Usage

- Register a new user account or log in with an existing account.
- Explore the available events on the home page.
- Register for events by clicking on the "Register" button.
- View your registered events in the "Registered Events" section.
- Superusers/admins can create and manage events through the admin interface.

## Contributing

Contributions are welcome! If you find any issues or have suggestions for improvements, please open an issue or submit a pull request.

## License

This project is licensed under the [MIT License](LICENSE).

## Contact

For any inquiries or questions, please contact [josh.gervais@itas.ca](mailto:josh.gervais@itas.ca).