#!/usr/bin/python3
""" Module to test Review class """

import unittest
from datetime import datetime
from .models.base_model import BaseModel
from .models.review import Review


class TestReviewClass(unittest.TestCase):

    """ Class that contains unittests for review.py """

    def setUp(self):
        """ Method to set up unittests """
        self.review1 = Review(text="Nice", place_id="", user_id="")
        self.review2 = Review()

    def test_assign_attr(self):
        """ Method to test instance attr """

        self.review2.text = "Awesome!"

        self.assertEqual(self.review2.text, "Awesome!")
        self.assertEqual(self.review1.text, "Nice")

    def test_review_type_attr(self):
        """ Method to test the type of review class attr """

        self.assertIs(type(self.review1.text), str)
        self.assertIs(type(self.review2.text), str)

    def test_has_attr(self):
        """ Method to test attr from BaseModel were inherited to review """

        self.assertTrue(hasattr(self.review1, "id"))
        self.assertTrue(hasattr(self.review1, "created_at"))
        self.assertTrue(hasattr(self.review1, "updated_at"))
        self.assertTrue(hasattr(self.review1, "text"))
        self.assertTrue(hasattr(self.review1, "place_id"))
        self.assertTrue(hasattr(self.review1, "user_id"))

        self.assertTrue(hasattr(self.review2, "id"))
        self.assertTrue(hasattr(self.review2, "created_at"))
        self.assertTrue(hasattr(self.review2, "updated_at"))
        self.assertTrue(hasattr(self.review2, "text"))
        self.assertTrue(hasattr(self.review2, "place_id"))
        self.assertTrue(hasattr(self.review2, "user_id"))

    def test_review_inherited_attr_type(self):
        """ Method to test inherited attr type """

        self.assertTrue(type(self.review1.id), str)
        self.assertTrue(type(self.review1.created_at), str)
        self.assertTrue(type(self.review1.updated_at), str)
        self.assertTrue(type(self.review2.id), str)
        self.assertTrue(type(self.review2.created_at), str)
        self.assertTrue(type(self.review2.updated_at), str)

    def test_review_does_dict(self):
        """ Method to test review with to_dict method """

        dict4 = self.review2.to_dict()
        newDict = Review(**dict4)

        self.assertEqual(newDict.id, self.review2.id)
        self.assertIsNot(newDict, self.review2)
        self.assertIsInstance(newDict.created_at, datetime)
        self.assertIsInstance(newDict.updated_at, datetime)

    def test_review_dir(self):
        """ Method to test if attrs in review """

        self.assertTrue('to_dict' in dir(self.review1))
        self.assertTrue('created_at' in dir(self.review1))
        self.assertTrue('updated_at' in dir(self.review1))
        self.assertTrue('id' in dir(self.review1))
        self.assertTrue('text' in dir(self.review1))
        self.assertTrue('user_id' in dir(self.review1))
        self.assertTrue('place_id' in dir(self.review1))

        self.assertTrue('to_dict' in dir(self.review2))
        self.assertTrue('created_at' in dir(self.review2))
        self.assertTrue('updated_at' in dir(self.review2))
        self.assertTrue('id' in dir(self.review2))
        self.assertTrue('text' in dir(self.review2))
        self.assertTrue('user_id' in dir(self.review2))
        self.assertTrue('place_id' in dir(self.review2))

    def test_review_update_at(self):
        """ Method to test updated at of review class """
        old1 = self.review1.updated_at
        old2 = self.review2.updated_at

        self.review1.save()
        self.review2.save()

        self.assertNotEqual(old1, self.review1.updated_at)
        self.assertNotEqual(old2, self.review2.updated_at)
