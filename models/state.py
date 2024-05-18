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
        all_cities = storage.all(City).values()

        state_cities = [city for city in all_cities
                        if city.state_id == self.id]

        return state_cities
