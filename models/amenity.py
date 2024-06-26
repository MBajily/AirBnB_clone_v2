#!/usr/bin/python3
"""the amenity class"""
from models.base_model import BaseModel, Base
from sqlalchemy.orm import relationship
from sqlalchemy import Column, String
from models.place import place_amenity
from models.review import Review
from models.place import Place
from models.city import City
from models.state import State


class Amenity(BaseModel, Base):
    """Represent an amenity.

    Attributes:
        name (str): name of amenity.
    """

    __tablename__ = "amenities"

    name = Column(String(128), nullable=False)
    place_amenities = relationship("Place", secondary=place_amenity)
