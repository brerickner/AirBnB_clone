#!/usr/bin/python3
""" Module to test City class """

import unittest
from datetime import datetime
from models.base_model import BaseModel
from models.city import City


class TestCityClass(unittest.TestCase):
    """ Class that contains unittests for city.py """

    def setUp(self):
        """ Method to set up unittests """
        self.city1 = City(name="Detroit")
        self.city2 = City()

    def test_assign_attr(self):
        """ Method to test instance attr """

        self.city2.name = "Tulsa"

        self.assertEqual(self.city2.name, "Tulsa")
        self.assertEqual(self.city1.name, "Detroit")

    def test_city_type_attr(self):
        """ Method to test the type of user class attr """

        self.assertIs(type(self.city1.name), str)
        self.assertIs(type(self.city2.name), str)

    def test_has_attr(self):
        """ Method to test that attr from BaseModel were inherited to City """

        self.assertTrue(hasattr(self.city1, "id"))
        self.assertTrue(hasattr(self.city1, "created_at"))
        self.assertTrue(hasattr(self.city1, "updated_at"))
        self.assertTrue(hasattr(self.city1, "name"))
        self.assertTrue(hasattr(self.city2, "id"))
        self.assertTrue(hasattr(self.city2, "created_at"))
        self.assertTrue(hasattr(self.city2, "updated_at"))
        self.assertTrue(hasattr(self.city2, "name"))

    def test_city_inherited_attr_type(self):
        """ Method to test inherited attr type """

        self.assertTrue(type(self.city1.id), str)
        self.assertTrue(type(self.city1.created_at), str)
        self.assertTrue(type(self.city1.updated_at), str)
        self.assertTrue(type(self.city2.id), str)
        self.assertTrue(type(self.city2.created_at), str)
        self.assertTrue(type(self.city2.updated_at), str)

    def test_city_does_dict(self):
        """ Method to test user with to_dict method """

        dict4 = self.city2.to_dict()
        newDict = City(**dict4)

        self.assertEqual(newDict.id, self.city2.id)
        self.assertIsNot(newDict, self.city2)
        self.assertIsInstance(newDict.created_at, datetime)
        self.assertIsInstance(newDict.updated_at, datetime)

    def test_city_dir(self):
        """ Method to test if attrs in City """

        self.assertTrue('to_dict' in dir(self.city1))
        self.assertTrue('created_at' in dir(self.city1))
        self.assertTrue('updated_at' in dir(self.city1))
        self.assertTrue('id' in dir(self.city1))
        self.assertTrue('name' in dir(self.city1))
        self.assertTrue('to_dict' in dir(self.city2))
        self.assertTrue('created_at' in dir(self.city2))
        self.assertTrue('updated_at' in dir(self.city2))
        self.assertTrue('id' in dir(self.city2))
        self.assertTrue('name' in dir(self.city2))

    def test_city_update_at(self):
        """ Method to test updated at of user class """
        old1 = self.city1.updated_at
        old2 = self.city2.updated_at

        self.city1.save()
        self.city2.save()

        self.assertNotEqual(old1, self.city1.updated_at)
        self.assertNotEqual(old2, self.city2.updated_at)
