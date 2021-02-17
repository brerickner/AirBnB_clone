#!/usr/bin/python3
""" Module to test File Storage Class """

import unittest
from datetime import datetime
from models.base_model import BaseModel
from models import FileStorage
import os
import models


class TestBaseClass(unittest.TestCase):

    """ Class that contains unittests for base_model.py """
    def setUp(self):
        """ Method to set up unittests """
        self.file = 'file.json'

        if os.path.isfile(self.file):
            os.remove(self.file)
        
        self.meow1 = BaseModel()
        self.meow2 = BaseModel(name="Bre", number="2326")
        self.meow3 = BaseModel(name="Aleia")
        self.meow4 = BaseModel(name=None, id=None, number=None)
        self.meow5 = BaseModel()
        self.storeMeow = FileStorage()
        self.allMeows = models.storage.all()
    
    def test_private(self):
        """Method to test if file storage attributes are private"""
        with self.assertRaises(AttributeError):
            self.meow1 = BaseModel().__file_path
        with self.assertRaises(AttributeError):
            self.meow1 = BaseModel().__objects

        with self.assertRaises(AttributeError):
            self.meow2 = BaseModel().__file_path
        with self.assertRaises(AttributeError):
            self.meow2 = BaseModel().__objects

        with self.assertRaises(AttributeError):
            self.meow3 = BaseModel().__file_path
        with self.assertRaises(AttributeError):
            self.meow3 = BaseModel().__objects

        with self.assertRaises(AttributeError):
            self.meow4 = BaseModel().__file_path
        with self.assertRaises(AttributeError):
            self.meow4 = BaseModel().__objects

    def test_attr_types(self):
        """ Method to test attr types for File storage """

        self.assertTrue(hasattr(FileStorage, "_FileStorage__file_path"))
        self.assertTrue(hasattr(FileStorage, "_FileStorage__objects"))
        
    def test_new_inst_attr(self):
        """ Method to test if instance of file storage inherits attr """
        self.storeMeow = FileStorage()
        self.assertTrue(hasattr(self.storeMeow, "_FileStorage__objects"))
        self.assertTrue(hasattr(self.storeMeow, "_FileStorage__file_path"))
    
    def test_has_attr(self):
        """ Method to test File Storage dict attrs """
        meowski = FileStorage()

        self.assertTrue(hasattr(meowski, "all"))
        self.assertTrue(hasattr(meowski, "new"))
        self.assertTrue(hasattr(meowski, "save"))
        self.assertTrue(hasattr(meowski, "reload"))

    def test_type_attr(self):
        """ Method to test type of priv attr """
        self.assertIs(type(models.storage._FileStorage__objects), dict)
        self.assertIs(type(models.storage._FileStorage__file_path), str)
