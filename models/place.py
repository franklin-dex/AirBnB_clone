#!/usr/bin/python3
"""This is the place class"""
from models.base_model import BaseModel

class Place(BaseModel):
    """This is the class for Place
    Attributes:
        city_id: city id
        user_id: user id
        name: name input
        description: string of description
        number_rooms: number of room in int
        number_bathrooms: number of bathrooms in int
        max_guest: maximum guest in int
        price_by_night:: pice for a staying in int
        latitude: latitude in flaot
        longitude: longitude in float
        amenity_ids: list of Amenity ids
    """

    city_id = ""
    user_id = ""
    name = ""
    description = ""
    number_rooms = int(0)
    number_bathrooms = int(0)
    max_guest = int(0)
    price_by_night = int(0)
    latitude = float(0.0)
    longitude = float(0.0)
    amenity_ids = []
