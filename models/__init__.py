#!/usr/bin/python3
"""create a unique FileStorage"""
from .engine.db_storage import DBStorage
from .engine.file_storage import FileStorage
from .base_model import BaseModel
from .amenity import Amenity
from .place import Place
from .review import Review
from .user import User
from .state import State
from .city import City
from os import getenv


if getenv("HBNB_TYPE_STORAGE") == "db":
    storage = DBStorage()

else:
    storage = FileStorage()

storage.reload()
