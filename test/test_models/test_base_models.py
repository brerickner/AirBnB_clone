#!/usr/bin/python3
""" Module to test BaseModel class """

import unittest
from datetime import datetime
from models.base_model import BaseModel

class TestBaseClass(unittest.TestCase):

    """ Class that contains unittests for base_model.py """
    
    def setUp(self):
        """ Method to set up unittests """
        self.meow1 = BaseModel()
        self.meow2 = BaseModel(name="Bre", number="2326")
        self.meow3 = BaseModel(name="Aleia")
        self.meow4 = BaseModel(name=None, id=None, number=None)
        self.meow5 = BaseModel()
        
    #**************UNLOCK AND SOLVE FOR FREE CHECKS********************
    def test_with_none(self):
        """ Method to test when **kwargs value is None """
        self.assertIsInstance(self.meow4.id, str)
        self.assertIsInstance(self.meow4.created_at, datetime)
        self.assertIsInstance(self.meow4.updated_at, datetime)
        self.assertNotEqual(self.meow3.id, self.meow4.id)
        self.assertNotEqual(self.meow1.id, self.meow4.id)

    def test_baseModel_init(self):
        """ Method to test unique id generated for base_model """

        self.assertIsInstance(self.meow1.created_at, datetime)
        self.assertIsInstance(self.meow2.created_at, datetime)
        self.assertIsInstance(self.meow3.created_at, datetime)
        self.assertIsInstance(self.meow1.updated_at, datetime)
        self.assertIsInstance(self.meow2.updated_at, datetime)
        self.assertIsInstance(self.meow3.updated_at, datetime)
        self.assertIsInstance(self.meow1.id, str)
        self.assertIsInstance(self.meow2.id, str)
        self.assertIsInstance(self.meow3.id, str)

    def test_id_unique(self):
        """ Method to test if id's are all unique from each other """
        self.assertNotEqual(self.meow1.id, self.meow3.id)
        self.assertNotEqual(self.meow1.id, self.meow2.id)
        self.assertNotEqual(self.meow3.id, self.meow2.id)

    def test_str_format(self):
        """ Method to test if str format is printing correctly """
        self.assertIsInstance(self.meow1, BaseModel)
        self.assertIsInstance(self.meow2, BaseModel)
        self.assertIsInstance(self.meow3, BaseModel)

    def test_base_attr(self):
        """ tests if instances can call attr """

        self.meow5.name = "Slim-Shady"
        self.meow5.my_number = 8

        self.assertEqual(self.meow5.name, "Slim-Shady")
        self.assertEqual(self.meow5.my_number, 8)
    
    def test_base_save(self):
        """ Method to test if updated after save """

        uptime1 = self.meow1.updated_at
        uptime2 = self.meow2.updated_at
        uptime3 = self.meow3.updated_at
        uptime4 = self.meow4.updated_at
        uptime5 = self.meow5.updated_at

        self.meow1.save()
        self.meow2.save()
        self.meow3.save()
        self.meow4.save()
        self.meow5.save()

        self.assertLess(uptime1, self.meow1.updated_at)
        self.assertLess(uptime2, self.meow2.updated_at)
        self.assertLess(uptime3, self.meow3.updated_at)
        self.assertLess(uptime4, self.meow4.updated_at)
        self.assertLess(uptime5, self.meow5.updated_at)

    def test_base_to_dict(self):
        """ Method to test dict method turned cls BaseModel into dict """

        self.assertIsNot(type(self.meow1), dict)
        self.assertIsNot(type(self.meow2), dict)
        self.assertIsNot(type(self.meow3), dict)
        self.assertIsNot(type(self.meow4), dict)
        self.assertIsNot(type(self.meow5), dict)

        meow1_json = self.meow1.to_dict()
        meow2_json = self.meow2.to_dict()
        meow3_json = self.meow3.to_dict()
        meow4_json = self.meow4.to_dict()
        meow5_json = self.meow5.to_dict()

        self.assertIs(type(meow1_json), dict)
        self.assertIs(type(meow2_json), dict)
        self.assertIs(type(meow3_json), dict)
        self.assertIs(type(meow4_json), dict)
        self.assertIs(type(meow5_json), dict)

    def test_json_key_type(self):
        """ Method to test if json keys are all strings """
        
        meow1_json = self.meow1.to_dict()
        meow2_json = self.meow2.to_dict()
        meow3_json = self.meow3.to_dict()
        meow4_json = self.meow4.to_dict()
        meow5_json = self.meow5.to_dict()

        for key in meow1_json.keys():
            self.assertEquals(type(meow1_json[key]), str)
            self.assertEquals(type(meow2_json[key]), str)
            self.assertEquals(type(meow3_json[key]), str)
            self.assertEquals(type(meow4_json[key]), str)
            self.assertEquals(type(meow5_json[key]), str)
   




"""

>>> my_mod.meow = "cat"
>>> print(my_mod.meow)
cat

>>> type(my_mod.number)
<class 'int'>

>>> type(my_mod.meow)
<class 'str'>

>>> print(type(my_mod.created_at))
<class 'datetime.datetime'>

>>> print(type(newMeow))
<class 'models.base_model.BaseModel'>

>>> print(type(newMeow.created_at))
<class 'datetime.datetime'>

>>> meow is newMeow
False

****creating new attribute for new meow***
>>> print(newMeow.name)

>>> newMeow.name = "MEE-OW"
>>> print(newMeow.name)
MEE-OW
>>> print(newMeow.to_dict())
{'updated_at': '2021-02-11T02:46:55.344351', 'name': 'MEE-OW', 'created_at': '2021-02-11T02:40:56.967147', 'id': '56087bb8-4a89-4e6d-8e6a-f60ddc2c871f', '__class__': 'BaseModel'}

>>> theNEWestmeow = BaseModel(**newestMeow)
>>> print(theNEWestmeow)
[BaseModel] (5d0d5322-bf4b-4d72-a067-accdd0a5b8da) {'updated_at': datetime.datetime(2021, 2, 11, 2, 55, 48, 194166), 'created_at': datetime.datetime(2021, 2, 11, 2, 55, 48, 194122), 'id': '5d0d5322-bf4b-4d72-a067-accdd0a5b8da'}
>>>

>>> theNEWestmeow = BaseModel(**newestMeow)
>>> print(theNEWestmeow)
[BaseModel] (5d0d5322-bf4b-4d72-a067-accdd0a5b8da) {'updated_at': datetime.datetime(2021, 2, 11, 2, 55, 48, 194166), 'created_at': datetime.datetime(2021, 2, 11, 2, 55, 48, 194122), 'id': '5d0d5322-bf4b-4d72-a067-accdd0a5b8da'}
>>> print(theNEWestmeow)
[BaseModel] (5d0d5322-bf4b-4d72-a067-accdd0a5b8da) {'updated_at': datetime.datetime(2021, 2, 11, 2, 55, 48, 194166), 'created_at': datetime.datetime(2021, 2, 11, 2, 55, 48, 194122), 'id': '5d0d5322-bf4b-4d72-a067-accdd0a5b8da'}

>>> print(newestMeow)
{'updated_at': '2021-02-11T02:46:55.344351', 'name': 'MEE-OW', 'created_at': '2021-02-11T02:40:56.967147', 'id': '56087bb8-4a89-4e6d-8e6a-f60ddc2c871f', '__class__': 'BaseModel'}
"""
