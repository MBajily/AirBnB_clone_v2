#!/usr/bin/python3
"""city class"""
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship
from models.place import Place


class City(BaseModel, Base):
    """Represent a city.
    Attributes:
        state_id (str): state id.
        name (str): name of city.
    """
    __tablename__ = "cities"

    name = Column(String(128), nullable=False)
    places = relationship("Place", cascade='all, delete, delete-orphan',
                          backref="cities")
    state_id = Column(String(60), ForeignKey('states.id'), nullable=False)
