#!/usr/bin/python3
""" new class DBStorage"""
from os import getenv
from sqlalchemy.orm import sessionmaker, scoped_session
from sqlalchemy import (create_engine)
from ..base_model import Base
from ..user import User
from ..place import Place
from ..review import Review
from ..amenity import Amenity
from ..state import State
from ..city import City



class DBStorage:
    """DBStorage"""
    __engine = None
    __session = None

    def __init__(self):
        user = getenv("HBNB_MYSQL_USER")
        passwd = getenv("HBNB_MYSQL_PWD")
        host = getenv("HBNB_MYSQL_HOST")
        env = getenv("HBNB_ENV")
        db = getenv("HBNB_MYSQL_DB")

        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'
                                      .format(user, passwd, host, db),
                                      pool_pre_ping=True)

        if (env == "test"):
            Base.metadata.drop_all(self.__engine)


    def all(self, cls=None):
        """returns all dictionaries

        Return:
            a dictionary of __object
        """
        dictionary = {}
        if cls:
            if type(cls) is str:
                cls = eval(cls)
            qry = self.__session.query(cls)

            for elem in qry:
                key = "{}.{}".format(type(elem).__name__, elem.id)
                dictionary[key] = elem

        else:
            list_a = [State, City, User, Place, Review, Amenity]

            for clase in list_a:
                qry = self.__session.query(clase)

                for elem in qry:
                    key = "{}.{}".format(type(elem).__name__, elem.id)
                    dictionary[key] = elem

        return (dictionary)


    def save(self):
        """save all changes
        """
        self.__session.commit()


    def delete(self, obj=None):
        """delete an element
        """
        if obj:
            self.session.delete(obj)


    def new(self, obj):
        """add a new element
        """
        self.__session.add(obj)


    def close(self):
        """ calls remove()
        """
        self.__session.close()


    def reload(self):
        """reload
        """
        Base.metadata.create_all(self.__engine)
        sec = sessionmaker(bind=self.__engine, expire_on_commit=False)
        Session = scoped_session(sec)
        self.__session = Session()
