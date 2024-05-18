#!/usr/bin/python3
""" City Module for HBNB project """
import os
from models.base_model import BaseModel


class City(BaseModel):
    """ The city class, contains state ID and name """
    state_id = ""
    name = ""

    def __init__(self, *args, **kwargs):
        """intializes the class"""
        super().__init__(*args, **kwargs)
