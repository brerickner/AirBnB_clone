#!/usr/bin/python3
""" Module to test Amenity class """

import unittest
from datetime import datetime
from models.base_model import BaseModel
from models.amenity import Amenity


class TestAmenityClass(unittest.TestCase):
    """ Class that contains unittests for amenity.py """

    def setUp(self):
        """ Method to set up unittests """
        self.amenity1 = Amenity(name="pool")
        self.amenity2 = Amenity()

    def test_assign_attr(self):
        """ Method to test instance attr """

        self.amenity2.name = "pet-friendly"

        self.assertEqual(self.amenity2.name, "pet-friendly")
        self.assertEqual(self.amenity1.name, "pool")

    def test_amenity_type_attr(self):
        """ Method to test the type of amenity class attr """

        self.assertIs(type(self.amenity1.name), str)
        self.assertIs(type(self.amenity2.name), str)

    def test_has_attr(self):
        """ Method to test attrs from BaseModel were inherited to amenity """

        self.assertTrue(hasattr(self.amenity1, "id"))
        self.assertTrue(hasattr(self.amenity1, "created_at"))
        self.assertTrue(hasattr(self.amenity1, "updated_at"))
        self.assertTrue(hasattr(self.amenity1, "name"))
        self.assertTrue(hasattr(self.amenity2, "id"))
        self.assertTrue(hasattr(self.amenity2, "created_at"))
        self.assertTrue(hasattr(self.amenity2, "updated_at"))
        self.assertTrue(hasattr(self.amenity2, "name"))

    def test_amenity_inherited_attr_type(self):
        """ Method to test inherited attr type """

        self.assertTrue(type(self.amenity1.id), str)
        self.assertTrue(type(self.amenity1.created_at), str)
        self.assertTrue(type(self.amenity1.updated_at), str)
        self.assertTrue(type(self.amenity2.id), str)
        self.assertTrue(type(self.amenity2.created_at), str)
        self.assertTrue(type(self.amenity2.updated_at), str)

    def test_amenity_does_dict(self):
        """ Method to test amenity with to_dict method """

        dict4 = self.amenity2.to_dict()
        newDict = Amenity(**dict4)

        self.assertEqual(newDict.id, self.amenity2.id)
        self.assertIsNot(newDict, self.amenity2)
        self.assertIsInstance(newDict.created_at, datetime)
        self.assertIsInstance(newDict.updated_at, datetime)

    def test_amenity_dir(self):
        """ Method to test if attrs in amenity """

        self.assertTrue('to_dict' in dir(self.amenity1))
        self.assertTrue('created_at' in dir(self.amenity1))
        self.assertTrue('updated_at' in dir(self.amenity1))
        self.assertTrue('id' in dir(self.amenity1))
        self.assertTrue('name' in dir(self.amenity1))
        self.assertTrue('to_dict' in dir(self.amenity2))
        self.assertTrue('created_at' in dir(self.amenity2))
        self.assertTrue('updated_at' in dir(self.amenity2))
        self.assertTrue('id' in dir(self.amenity2))
        self.assertTrue('name' in dir(self.amenity2))

    def test_amenity_update_at(self):
        """ Method to test updated at of amenity class """
        old1 = self.amenity1.updated_at
        old2 = self.amenity2.updated_at

        self.amenity1.save()
        self.amenity2.save()

        self.assertNotEqual(old1, self.amenity1.updated_at)
        self.assertNotEqual(old2, self.amenity2.updated_at)
