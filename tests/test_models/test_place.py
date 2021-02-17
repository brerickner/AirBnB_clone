#!/usr/bin/python3
""" Module to test place class """

import unittest
from datetime import datetime
from .models.base_model import BaseModel
from .models.place import Place


class TestPlaceClass(unittest.TestCase):

    """ Class that contains unittests for place.py """

    def setUp(self):
        """ Method to set up unittests """
        self.place1 = Place(city_id="",
                            user_id="",
                            name="Nice",
                            description="",
                            number_bathrooms=0,
                            max_guest=0,
                            price_by_night=0,
                            latitude=0.0,
                            longitude=0.0,
                            amenity_ids=[]
                            )
        self.place2 = Place()

    def test_assign_attr(self):
        """ Method to test instance attr """

        self.place2.name = "Awesome!"

        self.assertEqual(self.place2.name, "Awesome!")
        self.assertEqual(self.place1.name, "Nice")

    def test_place_type_attr(self):
        """ Method to test the type of place class attr """

        self.assertIs(type(self.place1.name), str)
        self.assertIs(type(self.place2.name), str)
        self.assertIs(type(self.place1.latitude), float)
        self.assertIs(type(self.place2.latitude), float)
        self.assertIs(type(self.place1.max_guest), int)
        self.assertIs(type(self.place2.max_guest), int)
        self.assertIs(type(self.place1.amenity_ids), list)
        self.assertIs(type(self.place2.amenity_ids), list)

    def test_has_attr(self):
        """ Method to test attr from BaseModel were inherited to place """

        self.assertTrue(hasattr(self.place1, "id"))
        self.assertTrue(hasattr(self.place1, "created_at"))
        self.assertTrue(hasattr(self.place1, "updated_at"))
        self.assertTrue(hasattr(self.place1, "name"))
        self.assertTrue(hasattr(self.place1, "city_id"))
        self.assertTrue(hasattr(self.place1, "user_id"))
        self.assertTrue(hasattr(self.place1, "description"))
        self.assertTrue(hasattr(self.place1, "number_rooms"))
        self.assertTrue(hasattr(self.place1, "number_bathrooms"))
        self.assertTrue(hasattr(self.place1, "max_guest"))
        self.assertTrue(hasattr(self.place1, "price_by_night"))
        self.assertTrue(hasattr(self.place1, "latitude"))
        self.assertTrue(hasattr(self.place1, "longitude"))
        self.assertTrue(hasattr(self.place1, "amenity_ids"))

        self.assertTrue(hasattr(self.place2, "id"))
        self.assertTrue(hasattr(self.place2, "created_at"))
        self.assertTrue(hasattr(self.place2, "updated_at"))
        self.assertTrue(hasattr(self.place2, "name"))
        self.assertTrue(hasattr(self.place2, "city_id"))
        self.assertTrue(hasattr(self.place2, "user_id"))
        self.assertTrue(hasattr(self.place2, "description"))
        self.assertTrue(hasattr(self.place2, "number_rooms"))
        self.assertTrue(hasattr(self.place2, "number_bathrooms"))
        self.assertTrue(hasattr(self.place2, "max_guest"))
        self.assertTrue(hasattr(self.place2, "price_by_night"))
        self.assertTrue(hasattr(self.place2, "latitude"))
        self.assertTrue(hasattr(self.place2, "longitude"))
        self.assertTrue(hasattr(self.place2, "amenity_ids"))

    def test_place_inherited_attr_type(self):
        """ Method to test inherited attr type """

        self.assertTrue(type(self.place1.id), str)
        self.assertTrue(type(self.place1.created_at), str)
        self.assertTrue(type(self.place1.updated_at), str)
        self.assertTrue(type(self.place1.city_id), str)
        self.assertTrue(type(self.place1.user_id), str)
        self.assertTrue(type(self.place1.description), str)
        self.assertTrue(type(self.place1.number_rooms), int)
        self.assertTrue(type(self.place1.number_bathrooms), int)
        self.assertTrue(type(self.place1.max_guest), int)
        self.assertTrue(type(self.place1.price_by_night), int)
        self.assertTrue(type(self.place1.latitude), float)
        self.assertTrue(type(self.place1.longitude), float)
        self.assertTrue(type(self.place1.amenity_ids), float)

        self.assertTrue(type(self.place2.id), str)
        self.assertTrue(type(self.place2.created_at), str)
        self.assertTrue(type(self.place2.updated_at), str)
        self.assertTrue(type(self.place2.city_id), str)
        self.assertTrue(type(self.place2.user_id), str)
        self.assertTrue(type(self.place2.description), str)
        self.assertTrue(type(self.place2.number_rooms), int)
        self.assertTrue(type(self.place2.number_bathrooms), int)
        self.assertTrue(type(self.place2.max_guest), int)
        self.assertTrue(type(self.place2.price_by_night), int)
        self.assertTrue(type(self.place2.latitude), float)
        self.assertTrue(type(self.place2.longitude), float)
        self.assertTrue(type(self.place2.amenity_ids), float)

    def test_place_does_dict(self):
        """ Method to test place with to_dict method """

        dict4 = self.place2.to_dict()
        newDict = Place(**dict4)

        self.assertEqual(newDict.id, self.place2.id)
        self.assertIsNot(newDict, self.place2)
        self.assertIsInstance(newDict.created_at, datetime)
        self.assertIsInstance(newDict.updated_at, datetime)

    def test_place_dir(self):
        """ Method to test if attrs in place """

        self.assertTrue('to_dict' in dir(self.place1))
        self.assertTrue('created_at' in dir(self.place1))
        self.assertTrue('updated_at' in dir(self.place1))
        self.assertTrue('id' in dir(self.place1))
        self.assertTrue('name' in dir(self.place1))
        self.assertTrue('user_id' in dir(self.place1))
        self.assertTrue('description' in dir(self.place1))
        self.assertTrue('number_rooms' in dir(self.place1))
        self.assertTrue('number_bathrooms' in dir(self.place1))
        self.assertTrue('max_guest' in dir(self.place1))
        self.assertTrue('price_by_night' in dir(self.place1))
        self.assertTrue('latitude' in dir(self.place1))
        self.assertTrue('longitude' in dir(self.place1))
        self.assertTrue('amenity_ids' in dir(self.place1))

        self.assertTrue('to_dict' in dir(self.place2))
        self.assertTrue('created_at' in dir(self.place2))
        self.assertTrue('updated_at' in dir(self.place2))
        self.assertTrue('id' in dir(self.place2))
        self.assertTrue('name' in dir(self.place2))
        self.assertTrue('user_id' in dir(self.place2))
        self.assertTrue('description' in dir(self.place2))
        self.assertTrue('number_rooms' in dir(self.place2))
        self.assertTrue('number_bathrooms' in dir(self.place2))
        self.assertTrue('max_guest' in dir(self.place2))
        self.assertTrue('price_by_night' in dir(self.place2))
        self.assertTrue('latitude' in dir(self.place2))
        self.assertTrue('longitude' in dir(self.place2))
        self.assertTrue('amenity_ids' in dir(self.place2))

    def test_place_update_at(self):
        """ Method to test updated at of place class """
        old1 = self.place1.updated_at
        old2 = self.place2.updated_at

        self.place1.save()
        self.place2.save()

        self.assertNotEqual(old1, self.place1.updated_at)
        self.assertNotEqual(old2, self.place2.updated_at)
