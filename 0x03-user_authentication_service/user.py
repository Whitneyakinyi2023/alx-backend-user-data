#!/usr/bin/env python3
"""
User model file.
This module defines a SQLAlchemy User model for user authentication.
"""


from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class User(Base):
    """
    SQLAlchemy model for users table.

    Attributes:
        id (int): The user's ID, which is the primary key.
        email (str): The user's email address.
        hashed_password (str): The hashed password for the user.
        session_id (str): Session ID for managing user sessions (nullable).
        reset_token (str): Token for password reset (nullable).
    """
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    email = Column(String(250), nullable=False)
    hashed_password = Column(String(250), nullable=False)
    session_id = Column(String(250), nullable=True)
    reset_token = Column(String(250), nullable=True)
