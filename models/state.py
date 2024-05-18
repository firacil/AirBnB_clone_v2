#!/usr/bin/python3
""" State Module for HBNB project """
import os
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from models import storage
from models.base_model import BaseModel, Base
from models.city import City


class State(BaseModel, Base):
    """ State class """
    @property
    def cities(self):
        """Returns the cities in this State"""
        cities_in_state = []
        for value in storage.all(City).values():
            if value.state_id == self.id:
                cities_in_state.append(value)
        return cities_in_state
