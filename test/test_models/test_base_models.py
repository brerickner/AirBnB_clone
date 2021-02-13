#!/usr/bin/python3
""" Module to test BaseModel class """

import unittest
from models.base_model import BaseModel

class TestBaseClass(unittest.TestCase):
	""" Class that contains unittests for base_model.py """
    def setUp(self):
        """ Method to set up unittests """
        self.meow1 = BaseModel(name="Bre", number="2326")
        self.meow2 = BaseModel(name="Aleia", number="2496")
        self.meow3 = BaseModel(name=None, id=None, number=None)
        self.meow4 = BaseModel(args=none, kwargs=None)


    def test_baseModel_init(self):
        """ Method to test unique id generated for base_model """
        self.assertIsInstance(self.meow1.id, str)
        self.assertIsInstance(self.meow1.created_at, datetime)
        self.assertIsInstance(self.meow1.updated_at, datetime)
        self.assertIsInstance(self.meow2.id, str)
        self.assertIsInstance(self.meow2.created_at, datetime)
        self.assertIsInstance(self.meow2.updated_at, datetime)
        self.assertIsInstance(self.meow3.id, str)
        self.assertIsInstance(self.meow3.created_at, datetime)
        self.assertIsInstance(self.meow3.updated_at, datetime)
        self.assertNotEqual(self.meow1.id, self.meow2.id)
        self.assertNotEqual(self.meow2.id, self.meow3.id)
        self.assertNotEqual(self.meow1.id, self.meow3.id)
        self.assertNotEqual(self.meow4.id, self.meow3.id)
        self.assertNotEqual(self.meow4.id, self.meow1.id)
        self.assertNotEqual(self.meow4.id, self.meow2.id)




"""
>>> type(my_mod.id)
<class 'str'>

>>> my_mod.meow = "cat"
>>> print(my_mod.meow)
cat


>>> print(my_mod.number)
89

>>> type(my_mod.number)
<class 'int'>

>>> type(my_mod.meow)
<class 'str'>

>>> my_mod = BaseModel()
>>> print(my_mod.to_dict())
{'id': 'addd9137-422a-4218-ab8b-22f5522fb92c', 'updated_at': '2021-02-11T00:14:25.297440', 'created_at': '2021-02-11T00:14:25.297412', '__class__': 'BaseModel'}


>>> print(my_mod)
[BaseModel] (addd9137-422a-4218-ab8b-22f5522fb92c) {'id': 'addd9137-422a-4218-ab8b-22f5522fb92c', 'updated_at': datetime.datetime(2021, 2, 11, 0, 14, 25, 297440), 'created_at': datetime.datetime(2021, 2, 11, 0, 14, 25, 297412)}

>>> print(type(my_mod.created_at))
<class 'datetime.datetime'>

>>> my_mod = BaseModel()
>>> my_mod.save()
>>> print(my_mod)
[BaseModel] (b8370e82-8545-40e2-ba35-d829d044284d) {'id': 'b8370e82-8545-40e2-ba35-d829d044284d', 'created_at': datetime.datetime(2021, 2, 11, 0, 59, 24, 129190), 'updated_at': datetime.datetime(2021, 2, 11, 0, 59, 28, 774668)}

""" check seconds later"""
>>> my_mod.save()
>>> print(my_mod)
[BaseModel] (b8370e82-8545-40e2-ba35-d829d044284d) {'id': 'b8370e82-8545-40e2-ba35-d829d044284d', 'created_at': datetime.datetime(2021, 2, 11, 0, 59, 24, 129190), 'updated_at': datetime.datetime(2021, 2, 11, 1, 0, 2, 630377)}

>>> my_mod = BaseModel()
>>> my_mod_json = my_mod.to_dict()
>>> print(my_mod_json)
{'__class__': 'BaseModel', 'updated_at': '2021-02-11T01:01:59.576551', 'created_at': '2021-02-11T01:01:59.576537', 'id': '4dcccf1d-b7af-4de6-a9b0-348c00eb7651'}

# after args and kwargs
>>> meow = BaseModel()
>>> meowJson = meow.to_dict()
>>> print(meowJson)
{'__class__': 'BaseModel', 'updated_at': '2021-02-11T02:37:09.069009', 'created_at': '2021-02-11T02:37:09.068379', 'id': '2a92ff85-3de8-45c4-9407-7aa550114bf1'}
>>>

>>> meow = BaseModel()
>>> meowJson = meow.to_dict()
>>> newMeow = BaseModel(**meowJson)
>>> print(newMeow)
[BaseModel] (56087bb8-4a89-4e6d-8e6a-f60ddc2c871f) {'updated_at': datetime.datetime(2021, 2, 11, 2, 40, 56, 967177), 'created_at': datetime.datetime(2021, 2, 11, 2, 40, 56, 967147), 'id': '56087bb8-4a89-4e6d-8e6a-f60ddc2c871f'}

>>> print(newMeow.id)
56087bb8-4a89-4e6d-8e6a-f60ddc2c871f

>>> print(type(newMeow))
<class 'models.base_model.BaseModel'>

>>> print(type(newMeow.created_at))
<class 'datetime.datetime'>

>>> meow is newMeow
False

>>> newMeow.save()
>>> print(newMeow)
[BaseModel] (56087bb8-4a89-4e6d-8e6a-f60ddc2c871f) {'updated_at': datetime.datetime(2021, 2, 11, 2, 46, 55, 344351), 'created_at': datetime.datetime(2021, 2, 11, 2, 40, 56, 967147), 'id': '56087bb8-4a89-4e6d-8e6a-f60ddc2c871f'}

""" creating new attribute for new meow"""
>>> print(newMeow.name)
Traceback (most recent call last):
	File "<stdin>", line 1, in <module>
AttributeError: 'BaseModel' object has no attribute 'name'
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
