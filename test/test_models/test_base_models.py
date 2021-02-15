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
        
    def test_private(self):
        """Method to test if basemodel attributes are private"""
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

    def test_with_none(self):
        """ Method to test when **kwargs value is None """
        self.assertIsInstance(self.meow4.id, str)
        self.assertIsInstance(self.meow4.created_at, datetime)
        self.assertIsInstance(self.meow4.updated_at, datetime)
        self.assertNotEqual(self.meow3.id, self.meow4.id)
        self.assertNotEqual(self.meow1.id, self.meow4.id)

    def test_init_type(self):
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
        self.assertNotEqual(self.meow4.id, self.meow3.id)
        self.assertNotEqual(self.meow4.id, self.meow1.id)
        self.assertNotEqual(self.meow4.id, self.meow2.id)

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

    def test_dict_class_attr(self):
        """ Method to test if to dict adds __class__ to attr """
        meow1_dict = self.meow1.to_dict()
        meow2_dict = self.meow2.to_dict()
        meow3_dict = self.meow3.to_dict()
        meow4_dict = self.meow4.to_dict()
        meow5_dict = self.meow5.to_dict()

        self.assertTrue(hasattr(self.meow1, "__class__"))
        self.assertTrue(hasattr(self.meow2, "__class__"))
        self.assertTrue(hasattr(self.meow3, "__class__"))
        self.assertTrue(hasattr(self.meow4, "__class__"))
        self.assertTrue(hasattr(self.meow5, "__class__"))

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

    def test_str_repr(self):
        """ Method to test is str repr is correct """
        
        testMeow1 = str(self.meow1).split(" ", 2)
        classMeow1 = "[{}]".format(self.meow1.__class__.__name__)
        idMeow1 = "({})".format(self.meow1.id)
        dictMeow1 = "{}".format(self.meow1.__dict__)
        
        testMeow2 = str(self.meow2).split(" ", 2)
        classMeow2 = "[{}]".format(self.meow2.__class__.__name__)
        idMeow2 = "({})".format(self.meow2.id)
        dictMeow2 = "{}".format(self.meow2.__dict__)
        
        testMeow3 = str(self.meow3).split(" ", 2)
        classMeow3 = "[{}]".format(self.meow3.__class__.__name__)
        idMeow3 = "({})".format(self.meow3.id)
        dictMeow3 = "{}".format(self.meow3.__dict__)
        
        testMeow4 = str(self.meow4).split(" ", 2)
        classMeow4 = "[{}]".format(self.meow4.__class__.__name__)
        idMeow4 = "({})".format(self.meow4.id)
        dictMeow4 = "{}".format(self.meow4.__dict__)

        self.assertEqual(classMeow1, testMeow1[0])
        self.assertEqual(idMeow1, testMeow1[1])
        self.assertEqual(dictMeow1, testMeow1[2])

        self.assertEqual(classMeow2, testMeow2[0])
        self.assertEqual(idMeow2, testMeow2[1])
        self.assertEqual(dictMeow2, testMeow2[2])

        self.assertEqual(classMeow3, testMeow3[0])
        self.assertEqual(idMeow3, testMeow3[1])
        self.assertEqual(dictMeow3, testMeow3[2])

        self.assertEqual(classMeow4, testMeow4[0])
        self.assertEqual(idMeow4, testMeow4[1])
        self.assertEqual(dictMeow4, testMeow4[2])

    def test_new_dict(self):
        """ Method to test when new dict is passed into BaseModel """
        meow1Json = self.meow1.to_dict()
        newMeow1 = BaseModel(**meow1Json)
        self.assertEqual(newMeow1.id, self.meow1.id)
        self.assertIsNot(newMeow1, self.meow1)
        self.assertIsInstance(newMeow1.created_at, datetime)
        self.assertIsInstance(newMeow1.updated_at, datetime)
        
        meow2Json = self.meow2.to_dict()
        newMeow2 = BaseModel(**meow2Json)
        self.assertEqual(newMeow2.id, self.meow2.id)
        self.assertIsNot(newMeow2, self.meow2)
        self.assertIsInstance(newMeow2.created_at, datetime)
        self.assertIsInstance(newMeow2.updated_at, datetime)
        
        meow3Json = self.meow3.to_dict()
        newMeow3 = BaseModel(**meow3Json)
        self.assertEqual(newMeow3.id, self.meow3.id)
        self.assertIsNot(newMeow3, self.meow3)
        self.assertIsInstance(newMeow3.created_at, datetime)
        self.assertIsInstance(newMeow3.updated_at, datetime)
        
        meow4Json = self.meow4.to_dict()
        newMeow4 = BaseModel(**meow4Json)
        self.assertEqual(newMeow4.id, self.meow4.id)
        self.assertIsNot(newMeow4, self.meow4)
        self.assertIsInstance(newMeow4.created_at, datetime)
        self.assertIsInstance(newMeow4.updated_at, datetime)

        meow5Json = self.meow5.to_dict()
        newMeow5 = BaseModel(**meow5Json)
        self.assertEqual(newMeow5.id, self.meow5.id)
        self.assertIsNot(newMeow5, self.meow5)
        self.assertIsInstance(newMeow5.created_at, datetime)
        self.assertIsInstance(newMeow5.updated_at, datetime)
        
        
        
"""

>>> my_mod.meow = "cat"
>>> print(my_mod.meow)
cat


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
