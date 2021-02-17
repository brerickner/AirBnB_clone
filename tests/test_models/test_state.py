#!/usr/bin/python3
""" Module to test State class """

import unittest
from datetime import datetime
from .models.base_model import BaseModel
from .models.state import State


class TestBaseClass(unittest.TestCase):

    """ Class that contains unittests for user.py """

    def setUp(self):
        """ Method to set up unittests """
        self.state1 = State(name="Michigan")
        self.state2 = State()

    def test_assign_attr(self):
        """ Method to test instance attr """

        self.state2.name = "Texas"

        self.assertEqual(self.state2.name, "Texas")
        self.assertEqual(self.state1.name, "Michigan")

    def test_state_type_attr(self):
        """ Method to test the type of user class attr """

        self.assertIs(type(self.state1.name), str)
        self.assertIs(type(self.state2.name), str)

    def test_has_attr(self):
        """ Method to test that attr from BaseModel were inherited to State """

        self.assertTrue(hasattr(self.state1, "id"))
        self.assertTrue(hasattr(self.state1, "created_at"))
        self.assertTrue(hasattr(self.state1, "updated_at"))
        self.assertTrue(hasattr(self.state1, "name"))
        self.assertTrue(hasattr(self.state2, "id"))
        self.assertTrue(hasattr(self.state2, "created_at"))
        self.assertTrue(hasattr(self.state2, "updated_at"))
        self.assertTrue(hasattr(self.state2, "name"))

    def test_state_inherited_attr_type(self):
        """ Method to test inherited attr type """

        self.assertTrue(type(self.state1.id), str)
        self.assertTrue(type(self.state1.created_at), str)
        self.assertTrue(type(self.state1.updated_at), str)
        self.assertTrue(type(self.state2.id), str)
        self.assertTrue(type(self.state2.created_at), str)
        self.assertTrue(type(self.state2.updated_at), str)

    def test_user_does_dict(self):
        """ Method to test user with to_dict method """

        dict4 = self.state2.to_dict()
        newDict = State(**dict4)

        self.assertEqual(newDict.id, self.state2.id)
        self.assertIsNot(newDict, self.state2)
        self.assertIsInstance(newDict.created_at, datetime)
        self.assertIsInstance(newDict.updated_at, datetime)

    def test_state_dir(self):
        """ Method to test if attrs in State """

        self.assertTrue('to_dict' in dir(self.state1))
        self.assertTrue('created_at' in dir(self.state1))
        self.assertTrue('updated_at' in dir(self.state1))
        self.assertTrue('id' in dir(self.state1))
        self.assertTrue('name' in dir(self.state1))

    def test_state_update_at(self):
        """ Method to test updated at of user class """
        old1 = self.state1.updated_at
        old2 = self.state2.updated_at

        self.state1.save()
        self.state2.save()

        self.assertNotEqual(old1, self.state1.updated_at)
        self.assertNotEqual(old2, self.state2.updated_at)
