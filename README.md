# Django-Blog-Application
using django , drf authentication

## Setup Instructions

1. Clone the repository:
    ```bash
    git clone <repository-url>
    cd blog_project
    ```

2. Create a virtual environment and install dependencies:
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    pip install -r requirements.txt
    ```

3. Apply migrations:
    ```bash
    python manage.py makemigrations
    python manage.py migrate
    ```

4. Create a superuser:
    ```bash
    python manage.py createsuperuser
    ```

5. Run the development server:
    ```bash
    python manage.py runserver
    ```

## API Documentation

### Authentication

- Obtain Token: `POST /api/token/`
- Refresh Token: `POST /api/token/refresh/`

### Posts

- List and Create: `GET, POST /api/posts/`
- Retrieve, Update, Delete: `GET, PUT, DELETE /api/posts/{id}/`

### Comments

- List and Create: `GET, POST /api/posts/{post_id}/comments/`
```

This setup should give you a functional Django blog application with basic CRUD functionalities and token-based authentication.