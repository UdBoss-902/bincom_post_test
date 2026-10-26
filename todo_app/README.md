# Task 2: PostgreSQL To-Do List Application

A command-line To-Do application built in Python that connects to a **PostgreSQL** database using `psycopg2` to perform full CRUD (Create, Read, Update, Delete) operations.

## Features
- **Persistent Storage**: Saves tasks securely inside a PostgreSQL database table (`todos`).
- **Automatic Table Setup**: Automatically creates the schema if it does not already exist.
- **Interactive CLI Menu**: Easily view, add, mark complete, and delete tasks.

## Prerequisites
- Python 3.x
- PostgreSQL installed and running locally
- The `psycopg2-binary` package

## Setup Instructions

1. Install the required Python package:
   ```bash
   pip install psycopg2-binary

2. Open todo_postgres.py and update the DB_CONFIG dictionary with your local PostgreSQL password:

DB_CONFIG = {
    "dbname": "postgres",
    "user": "postgres",
    "password": "your_actual_password",
    "host": "localhost",
    "port": "5432"
}

3. Run the application:
python todo_postgres.py