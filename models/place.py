#!/usr/bin/python3
"""This is the place class"""

from models.base_model import BaseModel, Base
from models.user import User
from models.city import City
import models

from sqlalchemy import Column, Integer, String, Float, ForeignKey
from sqlalchemy.orm import relationship, backref
from os import getenv

from sqlalchemy import *

metadata = Base.metadata

place_amenity = Table(
    'place_amenity', metadata,
    Column('place_id', String(60), ForeignKey('places.id'),
           nullable=False, primary_key=True),
    Column('amenity_id', String(60), ForeignKey('amenities.id'),
           nullable=False, primary_key=True))


class Place(BaseModel, Base):
    """ A place to stay """

    __tablename__ = "places"
    if getenv('HBNB_TYPE_STORAGE') == 'db':

        city_id = Column(String(60), ForeignKey("cities.id"), nullable=False)
        user_id = Column(String(60), ForeignKey("users.id"), nullable=False)
        name = Column(String(128), nullable=False)
        description = Column(String(1024), nullable=True)
        number_rooms = Column(Integer, nullable=False, default=0)
        number_bathrooms = Column(Integer, nullable=False, default=0)
        max_guest = Column(Integer, nullable=False, default=0)
        price_by_night = Column(Integer, nullable=False, default=0)
        latitude = Column(Float, nullable=True)
        longitude = Column(Float, nullable=True)
        amenity_ids = []
        reviews = relationship("Review", passive_deletes=True, backref="place")
        amenities = relationship(
            "Amenity", secondary=place_amenity, viewonly=False)
    else:
        city_id = ""
        user_id = ""
        name = ""
        description = ""
        number_rooms = 0
        number_bathrooms = 0
        max_guest = 0
        price_by_night = 0
        latitude = 0.0
        longitude = 0.0
        amenity_ids = []

    if getenv('HBNB_TYPE_STORAGE') != 'db':

        @property
        def reviews(self):
            """doc
            """
            my_dict = models.storage.all('Review')
            my_list = []
            for review in my_dict.values():
                if review.place_id == self.id:
                    my_list.append(review)

            return my_list

        @property
        def amenities(self):
            """
            returns the list of Amenity instances based on the
            attribute amenity_ids
            """
            my_dict = models.storage.all('Amenity')
            for amenity in my_dict.values():
                if amenity.place_id == self.id:
                    amenity_ids.append(amenity)
            return self.amenity_ids

        @amenities.setter
        def amenities(self, obj=None):
            """
            handles append method for adding an Amenity.id to the
            attribute amenity_ids
            """
            if type(obj) == 'Amenity':
                self.amenity_ids.append(obj.id)
