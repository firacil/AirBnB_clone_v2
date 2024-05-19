#!/usr/bin/python3
""" City Module for HBNB project """
import os
from sqlalchemy import Column, String, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from datetime import datetime
from models.base_model import BaseModel, Base


class City(BaseModel, Base):
    """ The city class, contains state ID and name """
    __tablename__ = 'cities'
    id = Column(String(60), primary_key=True, nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow, nullable=False)
    updated_at = Column(DateTime, default=datetime.utcnow, nullable=False, onupdate=datetime.utcnow)
    name = Column(String(128), nullable=False)
    state_id = Column(
        String(60),
        ForeignKey('states.id'),
        nullable=False
        )
    places = relationship(
        'Place',
        cascade='all, delete, delete-orphan',
        backref='city'
        )
