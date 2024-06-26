#!/usr/bin/python3
"""place class"""
from models.base_model import BaseModel, Base
from sqlalchemy import Column, Table, String, Integer, Float, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
from os import getenv
import models
from models.amenity import Amenity

place_amenity = Table("place_amenity", Base.metadata,
                      Column("place_id", String(60),
                             ForeignKey("places.id"),
                             primary_key=True,
                             nullable=False),
                      Column("amenity_id", String(60),
                             ForeignKey("amenities.id"),
                             primary_key=True,
                             nullable=False))


class Place(BaseModel, Base):
    """Represent a place.
    Attributes:
        city_id (str): City id.
        user_id (str): User id.
        name (str): name of place.
        description (str): description of place.
        number_rooms (int): number of rooms of place.
        number_bathrooms (int): number of bathrooms of place.
        max_guest (int): maximum number of guests of place.
        price_by_night (int): price by night of place.
        latitude (float): latitude of place.
        longitude (float): longitude of place.
        amenity_ids (list): A list of Amenity ids.
    """
    __tablename__ = "places"

    city_id = Column(String(60), ForeignKey("cities.id"), nullable=False)
    user_id = Column(String(60), ForeignKey("users.id"), nullable=False)
    name = Column(String(128), nullable=False)
    description = Column(String(1024))
    max_guest = Column(Integer, nullable=False, default=0)
    price_by_night = Column(Integer, nullable=False, default=0)
    latitude = Column(Float)
    longitude = Column(Float)
    number_bathrooms = Column(Integer, nullable=False, default=0)
    number_rooms = Column(Integer, nullable=False, default=0)    
    amenity_ids = []

    if getenv("HBNB_TYPE_STORAGE") == "db":
        reviews = relationship("Review", cascade='all, delete, delete-orphan',
                               backref="place")

        amenities = relationship("Amenity", secondary=place_amenity,
                                 viewonly=False,
                                 back_populates="place_amenities")

    else:
        @property
        def reviews(self):
            """ Returns list of reviews.id """
            var = models.storage.all()
            result = []
            list_a = []
            for key in var:
                rev = key.replace('.', ' ')
                rev = shlex.split(rev)
                if (rev[0] == 'Review'):
                    list_a.append(var[key])
            for elem in list_a:
                if (elem.place_id == self.id):
                    result.append(elem)
            return (result)

        @property
        def amenities(self):
            """ Returns list of amenity ids """
            return self.amenity_ids

        @amenities.setter
        def amenities(self, obj=None):
            """ Appends amenity ids to the attribute """
            if type(obj) is Amenity and obj.id not in self.amenity_ids:
                self.amenity_ids.append(obj.id)
