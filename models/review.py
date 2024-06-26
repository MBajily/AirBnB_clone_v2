#!/usr/bin/python3
"""review class"""
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from models.place import Place
from models.amenity import Amenity
from models.city import City
from models.state import State

class Review(BaseModel, Base):
    """Represent a review.
    Attributes:
        place_id (str): Place id.
        user_id (str): User id.
        text (str): text of review.
    """
    __tablename__ = "reviews"

    user_id = Column(String(60), ForeignKey("users.id"), nullable=False)
    text = Column(String(1024), nullable=False)
    place_id = Column(String(60), ForeignKey("places.id"), nullable=False)
