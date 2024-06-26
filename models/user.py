#!/usr/bin/python3
"""Defines the User class."""
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
# from models.place import Place
# from models.review import Review

class User(BaseModel, Base):
    """Represent a User.
    Attributes:
        email (str): The email
        password (str): The password
        first_name (str): The first name
        last_name (str): The last name
    """
    __tablename__ = "users"

    email = Column(String(128), nullable=False)
    password = Column(String(128), nullable=False)
    first_name = Column(String(128))
    last_name = Column(String(128))
    # reviews = relationship("Review", cascade='all, delete, delete-orphan',
    #                        backref="user")
    # places = relationship("Place", cascade='all, delete, delete-orphan',
    #                       backref="user")
