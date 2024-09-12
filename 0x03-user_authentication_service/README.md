# 0x03 User Authentication Service

This repository contains the code for a backend user authentication service, built using Python and Flask.

## Learning Objectives

By completing this project, you will be able to:
- Declare API routes in a Flask app
- Get and set cookies
- Retrieve request form data
- Return various HTTP status codes
- Implement basic user registration and login functionality
- Validate user credentials
- Manage user sessions using session IDs stored in cookies

## Requirements

- **Python**: 3.7
- **Libraries**:
  - Flask
  - SQLAlchemy 1.3.x
  - bcrypt
- **Code editor**: vi, vim, or emacs
- **Operating System**: Ubuntu 18.04 LTS

## Files

The repository contains the following files:

- `user.py`: Defines the `User` model for the database table `users`.
- `db.py`: Implements the `DB` class to interact with the SQLite database and manage user data.
- `auth.py`: Implements the `Auth` class which handles user authentication logic (registration, login, validation, session management).
- `app.py`: Defines the main Flask application, including routes for user registration, login, logout, and profile retrieval.

## Setup

1. **Clone the repository**:
   ```bash
   git clone https://github.com/alx-backend-user-data.git
   ```

2. **Navigate to the project directory**:
   ```bash
   cd 0x03-user_authentication_service
   ```

3. **Install the required libraries**:
   ```bash
   pip3 install flask sqlalchemy bcrypt
   ```

## Tasks

The project is divided into a series of mandatory tasks that guide you through implementing the user authentication service functionalities:

1. **User Model**:  
   Create a `User` model class in `user.py` representing a user in the database with attributes like `id`, `email`, `hashed_password`, `session_id`, and `reset_token`.

2. **Create User**:  
   Implement the `add_user` method in `db.py` to add a new user to the database, hashing their password before saving.

3. **Find User**:  
   Implement the `find_user_by` method in `db.py` to retrieve a user from the database based on provided criteria (e.g., email).

4. **Update User**:  
   Implement the `update_user` method in `db.py` to update a user's information in the database.

5. **Hash Password**:  
   Implement the `_hash_password` function in `auth.py` to hash a provided password using bcrypt.

6. **Register User**:  
   Implement the `register_user` method in `auth.py` to register a new user by checking for existing email, hashing the password, and saving the user data.

7. **Basic Flask App**:  
   Create a basic Flask application in `app.py` with a welcome message route.

8. **Register User (Endpoint)**:  
   Implement a POST endpoint `/users` in `app.py` to handle user registration requests, addressing both successful registrations and existing email cases.

9. **Credentials Validation**:  
   Implement the `valid_login` method in `auth.py` to validate login credentials (email and password) by finding the user and checking the hashed password.

10. **Generate UUIDs**:  
    Implement the `_generate_uuid` function in `auth.py` to generate unique session IDs as UUID strings.

11. **Get Session ID**:  
    Implement the `create_session` method in `auth.py` to create a new session for a user by generating a UUID, storing it in the database, and returning the session ID.

12. **Log In (Endpoint)**:  
    Implement a POST endpoint `/sessions` in `app.py` to handle login requests. Validate credentials, create a session if successful, set a session ID cookie, and return a success message.

13. **Find User by Session ID**:  
    Implement the `get_user_from_session_id` method in `auth.py` to retrieve a user object based on a provided session ID.

14. **Destroy Session**:  
    Implement the `destroy_session` method in `auth.py` to remove a user's session ID from the database, effectively logging them out.

15. **Log Out (Endpoint)**:  
    Implement a DELETE endpoint `/sessions` in `app.py` to handle logout requests. Retrieve the user based on the session ID cookie, destroy the session, and redirect to the homepage.

16. **User Profile (Endpoint)**:  
    Implement a GET endpoint `/profile` in `app.py` to retrieve a user's profile information. Validate the session ID cookie and return the user's email.

