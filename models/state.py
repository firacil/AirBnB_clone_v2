#!/usr/bin/python3
""" State Module for HBNB project """
import os
from sqlalchemy import Column, String, DateTime
from sqlalchemy.orm import relationship
from datetime import datetime
from models.base_model import BaseModel, Base
from models.city import City
from os import environ
import models


class State(BaseModel, Base):
    """ State class """
    __tablename__ = 'states'
    name = Column(String(128), nullable=False)

    if environ['HBNB_TYPE_STORAGE'] == 'db':
        cities = relationship('City', cascade='all, delete', backref='state')

    else:
        @property
        def cities(self):
            """Returns the cities in this State"""
            from models import storage
            cities_in_state = []
            for value in storage.all(City).values():
                if value.state_id == self.id:
                    cities_in_state.append(value)
            return cities_in_state
