# REST API Fundamentals (Project 1)

## About
A stateless REST API built with FastAPI for the DecodeLabs Backend Development training. It manages a list of users using GET, POST, PUT and DELETE, and sends and receives JSON. Data is stored in memory, so it resets when the server restarts.

## How to Run
```
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
uvicorn main:app --reload
```
Open http://127.0.0.1:8000/docs to test the API.

## Endpoints

| Method | Endpoint | Action | Success Code |
|--------|----------|--------|--------------|
| GET | /users | List all users | 200 |
| GET | /users/{id} | Get one user | 200 |
| POST | /users | Create a user | 201 |
| PUT | /users/{id} | Update a user | 200 |
| DELETE | /users/{id} | Delete a user | 204 |

Errors: 404 if the user is not found, 422 if the data is invalid.

## Why FastAPI
I chose FastAPI because it validates JSON automatically with Pydantic and creates test documentation at /docs. It is also faster than Flask and easy to write in Python.

## Author
Devisrujana
