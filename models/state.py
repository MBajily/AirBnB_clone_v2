#!/usr/bin/python3
"""This is the state class"""
from models.base_model import BaseModel, Base
from sqlalchemy.orm import relationship
from sqlalchemy import Column, String
import models
import shlex
from models.review import Review
from models.amenity import Amenity
from models.city import City
from models.place import Place

class State(BaseModel, Base):
    """Represent a state.

    Attributes:
        name (str): The name
    """
    __tablename__ = "states"

    name = Column(String(128), nullable=False)
    cities = relationship("City", cascade='all, delete, delete-orphan',
                          backref="state")

    @property
    def cities(self):
        var = models.storage.all()
        result = []
        list_a = []

        for key in var:
            city = key.replace('.', ' ')
            city = shlex.split(city)

            if (city[0] == 'City'):
                list_a.append(var[key])

        for element in list_a:
            if (element.state_id == self.id):
                result.append(element)

        return (result)
