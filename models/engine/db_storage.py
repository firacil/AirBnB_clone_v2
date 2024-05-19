#!/usr/bin/python3
"""This module defines a class to manage database storage for hbnbclone"""
import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
import urllib.parse

from models.base_model import BaseModel, Base
from models.state import State
from models.city import City
from models.user import User
from models.place import Place
from models.amenity import Amenity
from models.review import Review
name_class = {
        'Amenity': Amenity,
        'City': City,
        'Place': Place,
        'State': State,
        'Review': Review,
        'User': User
}


class DBStorage:
    """This class manages storage of hbnb models in a SQL database"""
    __engine = None
    __session = None

    def __init__(self):
        """Initializes the SQL database storage"""
        user = os.getenv('HBNB_MYSQL_USER')
        pword = os.getenv('HBNB_MYSQL_PWD')
        host = os.getenv('HBNB_MYSQL_HOST')
        db_name = os.getenv('HBNB_MYSQL_DB')
        DATABASE_URL = "mysql+mysqldb://{}:{}@{}/{}".format(
            user, pword, host, db_name
        )
        self.__engine = create_engine(DATABASE_URL)
        if os.getenv('HBNB_ENV') == 'test':
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """Returns a dictionary of models currently in storage"""
        if not self.__session:
            self.reload()
        objects = {}
        if type(cls) == str:
            cls = name_class.get(cls, None)
        if cls:
            for obj in self.__session.query(cls):
                objects[obj.__class__.__name__ + '.' + obj.id] = obj
        else:
            for cls in name_class.values():
                for obj in self.__session.query(cls):
                    objects[obj.__class__.__name__ + '.' + obj.id] = obj
        return objects

    def delete(self, obj=None):
        """Removes an object from the storage database"""
        if not self.__session:
            self.reload()
        if obj:
            self.__session.delete(obj)

    def new(self, obj):
        """Adds new object to storage database"""
        self.__session.add(obj)

    def save(self):
        """Commits the session changes to database"""
        self.__session.commit()

    def reload(self):
        """Loads storage database"""
        session_factory = sessionmaker(bind=self.__engine,
                                       expire_on_commit=False)
        Base.metadata.create_all(self.__engine)
        self.__session = scoped_session(session_factory)

    def close(self):
        """Closes the storage engine."""
        self.__session.remove()
