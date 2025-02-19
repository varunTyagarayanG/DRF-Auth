# Django REST Framework Authentication API

## Overview

This is a simple authentication API built using Django Rest Framework (DRF) and JWT (JSON Web Token). It provides user registration, login, token-based authentication, and a protected route that requires authentication.

## Features

- **User Registration**
- **User Login with JWT Authentication**
- **Token Refresh**
- **Protected Route (Accessible only with a valid token)**

## Setup & Installation

### 1. Clone the Repository

```sh
git clone <repo-url>
cd auth_project
```

### 2. Create a Virtual Environment (Optional but Recommended)

```sh
python -m venv venv
source venv/bin/activate  
venv\Scripts\activate   
```

### 3. Install Dependencies

```sh
pip install django djangorestframework djangorestframework-simplejwt
```

### 4. Run Migrations

```sh
python manage.py makemigrations accounts
python manage.py migrate
```

### 5. Start the Server

```sh
python manage.py runserver
```

## API Endpoints

### 1️⃣ Register a User

- **URL:** `POST /api/auth/register/`
- **Request Body:**

```json
{
  "username": "testuser",
  "email": "test@example.com",
  "password": "password123"
}
```

- **Response:**

```json
{
  "id": 1,
  "username": "testuser",
  "email": "test@example.com"
}
```

### 2️⃣ Login (Get JWT Tokens)

- **URL:** `POST /api/auth/login/`
- **Request Body:**

```json
{
  "username": "testuser",
  "password": "password123"
}
```

- **Response:**

```json
{
  "refresh": "your_refresh_token_here",
  "access": "your_access_token_here"
}
```

### 3️⃣ Refresh Access Token

- **URL:** `POST /api/auth/refresh/`
- **Request Body:**

```json
{
  "refresh": "your_refresh_token_here"
}
```

- **Response:**

```json
{
  "access": "new_access_token_here"
}
```

### 4️⃣ Protected Route (Requires Authentication)

- **URL:** `GET /api/auth/protected/`
- **Headers:**

```json
{
  "Authorization": "Bearer your_access_token_here"
}
```

- **Response (if authenticated):**

```json
{
  "message": "You have access to this protected route"
}
```

- **Response (if unauthorized):**

```json
{
  "detail": "Authentication credentials were not provided."
}
```

## Project Structure

```
/auth_project/
│── accounts/
│   ├── migrations/
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── serializers.py
│   ├── tests.py
│   ├── urls.py
│   ├── views.py
│── auth_project/
│   ├── __init__.py
│   ├── asgi.py
│   ├── settings.py
│   ├── urls.py
│   ├── wsgi.py
│── manage.py
```

## Next Steps

- Implement logout functionality by blacklisting the refresh token.
- Add additional user profile fields.
- Implement role-based access control (RBAC).


## Author

Developed by **G Varun Tyagarayan** 🚀