#!/usr/env/python3
import json

""" This module creates a class to manage file storage """


class FileStorage:
    """ This class manages file storage for other classes """

    self.__file_path = file.json
    self.__objects = {}


    # DO THESE NEED TO BE INSTANCE METHODS OR CLASS METHODS?
    def all(self):
        """ Returns the dictionary stored in __objects """
        return self.objects()

    def new(self, obj):
        """ Sets obj with key <obj class name>.id in __objects """
        ident = "{}.{}".format(obj.__class__.__name__, obj.id())
        self.__objects[obj] = ident

    def save(self):
        """ Serializes __objects to the JSON file """
        with open(cls.__name__ + ".json", 'w') as f:
            # I don't fully understand where we're getting the value to save
            if self.to_dict() is not None and len(list_objs) > 0:
                f.write(json.dumps(self.to_dict())

    def reload(self):
        """ deserializes the JSON file to __objects """
        lst = []
        # Same issue as above. Not fully sure what we're checking
        jstr = ""
        try:
            f = open(cls.__name__ + ".json", 'r')
            for line in f:
                jstr += line
            if jstr is None or len(json_string) < 1:
                        return
            self.__obj = json.load(jstr)
            f.close()
            return olst
        except:
            return
