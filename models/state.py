#!/usr/bin/python3
"""This is the state class"""
from models.base_model import BaseModel, Base
from sqlalchemy.orm import relationship
from sqlalchemy import Column, String
from sqlalchemy.ext.declarative import declarative_base
import models
import shlex
from models.city import City


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
