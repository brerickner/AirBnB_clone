#!/usr/bin/python3
"""This module creates a base class"""
import json
import csv
import uuid
import datetime

class BaseModel:
    """ This class defines all common attributes for other classes """

    def __init__(self):
        #id = uuid string created when instance is created
        self.id = str(uuid.uuid4())
        #created_at: datetime when created
        self.created_at = datetime.datetime.today
        #updated_at: updates every time changed
        self.updated_at = datetime.datetime.today

    def __str__(self):
        """This sets the string format"""
        return "[{}] ({}) <{}>".format(self.__class__.__name__, self.id, self.__dict__)

    # Public Method
    def save(self):
        """ Updates the public instance attribute updated_at with the current
        datetime """
        self.updated_at = datetime.datetime.today

    # Public Method
    def to_dict(self):
        """ Returns a dictionary containing all keys/values of
        __dict__ of the instance """
        newdict = self.__dict__.copy()
        newdict["__class__"] = self.__class__.__name__
        newdict["created_at"] = datetime.datetime.isoformat(self.created_at())
        newdict["updated_at"] = datetime.datetime.isoformat(self.updated_at())

        return newdict
