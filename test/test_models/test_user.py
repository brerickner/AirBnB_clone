#!/usr/bin/python3
""" Module to test User class """

import unittest
from datetime import datetime
from .models.base_model import BaseModel
from .models.user import User


class TestBaseClass(unittest.TestCase):

    """ Class that contains unittests for user.py """

    def setUp(self):
        """ Method to set up unittests """
        self.usr1 = User()
        self.usr2 = User(first_name="Aleia")
        self.usr3 = User(first_name=None, email=None, password=None)
        self.usr4 = User(last_name="Rickner")
        self.blankUsr = User()

    def test_assign_attr(self):
        """ Method to test instance attr """

        self.usr1.first_name = "ME"
        self.usr1.email = "meow@fakegmail.com"
        self.usr1.password = "bark"
        self.usr1.last_name = "OW"

        self.usr2.first_name = "Aleia"
        self.usr2.email = "aleia@fakegmail.com"
        self.usr2.password = "meeeow!"
        self.usr2.last_name = "Mcnaney Devore"

        self.usr3.first_name = "Chicka-Chicka"
        self.usr3.email = "slim@fakegmail.com"
        self.usr3.password = "m&m"
        self.usr3.last_name = "Slim-Shady"

        self.usr4.first_name = "Bre"
        self.usr4.email = "bre@fakegmail.com"
        self.usr4.password = "meow"
        self.usr4.last_name = "Rickner"

        self.assertEqual(self.usr1.first_name, "ME")
        self.assertEqual(self.usr1.email, "meow@fakegmail.com")
        self.assertEqual(self.usr1.password, "bark")
        self.assertEqual(self.usr1.last_name, "OW")

        self.assertEqual(self.usr2.first_name, "Aleia")
        self.assertEqual(self.usr2.email, "aleia@fakegmail.com")
        self.assertEqual(self.usr2.password, "meeeow!")
        self.assertEqual(self.usr2.last_name, "Mcnaney Devore")

        self.assertEqual(self.usr3.first_name, "Chicka-Chicka")
        self.assertEqual(self.usr3.email, "slim@fakegmail.com")
        self.assertEqual(self.usr3.password, "m&m")
        self.assertEqual(self.usr3.last_name, "Slim-Shady")

        self.assertEqual(self.usr4.first_name, "Bre")
        self.assertEqual(self.usr4.email, "bre@fakegmail.com")
        self.assertEqual(self.usr4.password, "meow")
        self.assertEqual(self.usr4.last_name, "Rickner")

    def test_type_attr(self):
        """ Method to test the type of user class attr """

        self.assertIs(type(self.usr1.first_name), str)
        self.assertIs(type(self.usr1.last_name), str)
        self.assertIs(type(self.usr1.password), str)
        self.assertIs(type(self.usr1.email), str)

        self.assertIs(type(self.usr2.first_name), str)
        self.assertIs(type(self.usr2.last_name), str)
        self.assertIs(type(self.usr2.password), str)
        self.assertIs(type(self.usr2.email), str)

        self.assertIs(type(self.usr3.first_name), str)
        self.assertIs(type(self.usr3.last_name), str)
        self.assertIs(type(self.usr3.password), str)
        self.assertIs(type(self.usr3.email), str)

        self.assertIs(type(self.usr4.first_name), str)
        self.assertIs(type(self.usr4.last_name), str)
        self.assertIs(type(self.usr4.password), str)
        self.assertIs(type(self.usr4.email), str)

    def test_usr_type(self):
        """ Method to test User inherited BaseModel type """

        self.assertTrue(type(self.usr1), BaseModel)
        self.assertTrue(type(self.usr2), BaseModel)
        self.assertTrue(type(self.usr3), BaseModel)
        self.assertTrue(type(self.usr4), BaseModel)
        self.assertTrue(type(self.blankUsr), BaseModel)
        self.assertTrue(type(self.usr1), User)
        self.assertTrue(type(self.usr2), User)
        self.assertTrue(type(self.usr3), User)
        self.assertTrue(type(self.usr4), User)
        self.assertTrue(type(self.blankUsr), User)

    def test_empty_user(self):
        """ Method to test empty kwarg user """

        self.assertEqual(self.blankUsr.first_name, "")
        self.assertEqual(self.blankUsr.last_name, "")
        self.assertEqual(self.blankUsr.password, "")
        self.assertEqual(self.blankUsr.email, "")

    def test_has_attr(self):
        """ Method to test that attr from BaseModel were inherited to User """

        self.assertTrue(hasattr(self.usr1, "id"))
        self.assertTrue(hasattr(self.usr1, "created_at"))
        self.assertTrue(hasattr(self.usr1, "updated_at"))
        self.assertTrue(hasattr(self.usr1, "first_name"))
        self.assertTrue(hasattr(self.usr1, "last_name"))
        self.assertTrue(hasattr(self.usr1, "email"))
        self.assertTrue(hasattr(self.usr1, "password"))

        self.assertTrue(hasattr(self.usr2, "id"))
        self.assertTrue(hasattr(self.usr2, "created_at"))
        self.assertTrue(hasattr(self.usr2, "updated_at"))
        self.assertTrue(hasattr(self.usr2, "first_name"))
        self.assertTrue(hasattr(self.usr2, "last_name"))
        self.assertTrue(hasattr(self.usr2, "email"))
        self.assertTrue(hasattr(self.usr2, "password"))

        self.assertTrue(hasattr(self.usr3, "id"))
        self.assertTrue(hasattr(self.usr3, "created_at"))
        self.assertTrue(hasattr(self.usr3, "updated_at"))
        self.assertTrue(hasattr(self.usr3, "first_name"))
        self.assertTrue(hasattr(self.usr3, "last_name"))
        self.assertTrue(hasattr(self.usr3, "email"))
        self.assertTrue(hasattr(self.usr3, "password"))

        self.assertTrue(hasattr(self.usr4, "id"))
        self.assertTrue(hasattr(self.usr4, "created_at"))
        self.assertTrue(hasattr(self.usr4, "updated_at"))
        self.assertTrue(hasattr(self.usr4, "first_name"))
        self.assertTrue(hasattr(self.usr4, "last_name"))
        self.assertTrue(hasattr(self.usr4, "email"))
        self.assertTrue(hasattr(self.usr4, "password"))

        self.assertTrue(hasattr(self.blankUsr, "id"))
        self.assertTrue(hasattr(self.blankUsr, "created_at"))
        self.assertTrue(hasattr(self.blankUsr, "updated_at"))
        self.assertTrue(hasattr(self.blankUsr, "first_name"))
        self.assertTrue(hasattr(self.blankUsr, "last_name"))
        self.assertTrue(hasattr(self.blankUsr, "email"))
        self.assertTrue(hasattr(self.blankUsr, "password"))

    def test_inherited_attr_type(self):
        """ Method to test inherited attr type """

        self.assertTrue(type(self.usr1.id), str)
        self.assertTrue(type(self.usr1.created_at), str)
        self.assertTrue(type(self.usr1.updated_at), str)

    def test_user_does_dict(self):
        """ Method to test user with to_dict method """
        aDict = self.blankUsr.to_dict()
        dict1 = self.usr1.to_dict()
        dict2 = self.usr2.to_dict()
        dict3 = self.usr3.to_dict()
        dict4 = self.usr4.to_dict()
        newDict = User(**dict4)

        self.assertEqual(newDict.id, self.usr4.id)
        self.assertIsNot(newDict, self.usr4)
        self.assertIsInstance(newDict.created_at, datetime)
        self.assertIsInstance(newDict.updated_at, datetime)

        self.assertIs(type(aDict), dict)
        self.assertIs(type(dict1), dict)
        self.assertIs(type(dict2), dict)
        self.assertIs(type(dict3), dict)
        self.assertIs(type(dict4), dict)

    def test_user_dir(self):
        """ Method to test if attrs in User """
        self.assertTrue('to_dict' in dir(self.usr1))
        self.assertTrue('created_at' in dir(self.usr1))
        self.assertTrue('updated_at' in dir(self.usr1))
        self.assertTrue('id' in dir(self.usr1))
        self.assertTrue('password' in dir(self.usr1))
        self.assertTrue('email' in dir(self.usr1))
        self.assertTrue('first_name' in dir(self.usr1))
        self.assertTrue('last_name' in dir(self.usr1))

    def test_user_update_at(self):
        """ Method to test updated at of user class """

        old1 = self.usr1.updated_at
        old2 = self.usr2.updated_at
        old3 = self.usr3.updated_at
        old4 = self.usr4.updated_at
        old5 = self.blankUsr.updated_at

        self.usr1.save()
        self.usr2.save()
        self.usr3.save()
        self.usr4.save()
        self.blankUsr.save()

        self.assertNotEqual(old1, self.usr1.updated_at)
        self.assertNotEqual(old2, self.usr2.updated_at)
        self.assertNotEqual(old3, self.usr3.updated_at)
        self.assertNotEqual(old4, self.usr4.updated_at)
        self.assertNotEqual(old5, self.blankUsr.updated_at)
