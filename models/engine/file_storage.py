#!/usr/env/python3
""" This module creates a class to manage file storage """

from models import BaseModel
from models.user import User
from models.city import City
from models.state import State
from models.amenity import Amenity
from models.place import Place
from models.review import Review

import json
from os import path


class FileStorage:

    """ This class manages file storage for other classes """

    __file_path = 'file.json'
    __objects = {}
    classies = {'BaseModel': BaseModel,
                'User': User,
                'State': State,
                'City': City,
                'Amenity': Amenity,
                'Place': Place,
                'Review': Review
                }

    # DO THESE NEED TO BE INSTANCE METHODS OR CLASS METHODS?
    def all(self):
        """ Returns the dictionary stored in __objects """
        return self.__objects

    def new(self, obj):
        """ Sets obj with key <obj class name>.id in __objects """
        FileStorage.__objects["{}.{}".
                              format(obj.__class__.__name__, obj.id)] = obj

    def save(self):
        """ Serializes __objects to the JSON file """

        # I don't fully understand where we're getting the value to save

        newDict = {}
        for k, v in FileStorage.__objects.items():
            newDict[k] = v.to_dict()
        with open(FileStorage.__file_path, mode='w') as f:
            json.dump(newDict, f)

    def reload(self):
        """ deserializes the JSON file to __objects """
        if path.isfile(self.__file_path):
            with open(FileStorage.__file_path, mode='r') as f:
                fromFile = json.load(f)
                for k, v in fromFile.items():
                    newStuff = fromFile[k]["__class__"]
                    newClass = self.classies[newStuff]
                    self.__objects[k] = newClass(**v)
        if path.isfile(self.__file_path) is False:
            return
