#!/usr/bin/python3
""" State Module for HBNB project """

import models
from models.base_model import BaseModel, Base
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship, backref
from os import getenv


class State(BaseModel, Base):
    """ State class """

    __tablename__ = 'states'
    if getenv('HBNB_TYPE_STORAGE') == 'db':
        name = Column(String(128), nullable=False)
        cities = relationship('City', cascade='all, delete', backref='state')
    else:
        name = ""

        "getter method"
        @property
        def cities(self):
            """ Return the list of City object linked to the current State"""
            cities_list = []
            for city in models.storage.all(City).values():

                if city.state_id == self.id:
                    cities_list.append(city)

            return cities_list
