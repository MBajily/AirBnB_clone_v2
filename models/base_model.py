#!/usr/bin/python3
"""base model class for AirBnB"""
from sqlalchemy.ext.declarative import declarative_base
import uuid
import models
from datetime import datetime
from sqlalchemy import Column, String, DateTime


Base = declarative_base()


class BaseModel:
    """Represents the BaseModel of the HBnB project."""
    id = Column(String(60), unique=True, nullable=False, primary_key=True)
    updated_at = Column(DateTime, nullable=False, default=(datetime.utcnow()))
    created_at = Column(DateTime, nullable=False, default=(datetime.utcnow()))


    def __init__(self, *args, **kwargs):
        """Initialize a new BaseModel.

        Args:
            kwargs: arguments for the constructor
            args: not used
        Attributes:
            id: unique id
            updated_at: updated date
            created_at: creation date
        """
        if kwargs:
            for key, value in kwargs.items():
                if key == "created_at" or key == "updated_at":
                    value = datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f")

                if key != "__class__":
                    setattr(self, key, value)

            if "id" not in kwargs:
                self.id = str(uuid.uuid4())

            if "updated_at" not in kwargs:
                self.updated_at = datetime.now()

            if "created_at" not in kwargs:
                self.created_at = datetime.now()

        else:
            self.id = str(uuid.uuid4())
            self.created_at = self.updated_at = datetime.now()


    def __str__(self):
        """returns a string
        Return:
            returns a string of class name, id, and dictionary
        """
        return "[{}] ({}) {}".format(
            type(self).__name__, self.id, self.__dict__)


    def __repr__(self):
        """return a string representaion
        """
        return self.__str__()


    def to_dict(self):
        """creates dictionary of the class  and returns
        Return:
            returns a dictionary of all the key values in __dict__
        """
        dictionary = dict(self.__dict__)
        dictionary["__class__"] = str(type(self).__name__)
        dictionary["updated_at"] = self.updated_at.isoformat()
        dictionary["created_at"] = self.created_at.isoformat()

        if '_sa_instance_state' in dictionary.keys():
            del dictionary['_sa_instance_state']

        return dictionary


    def save(self):
        """updates the public instance attribute updated_at to current
        """
        self.updated_at = datetime.now()
        models.storage.new(self)
        models.storage.save()


    def delete(self):
        """ delete object
        """
        models.storage.delete(self)
