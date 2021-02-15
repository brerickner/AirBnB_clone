#!/usr/bin/python3
from models import BaseModel
import cmd
""" This module creates the console class """


class HBNBCommand(cmd.Cmd):
    """ This class creates an interactive console """

    prompt = "(hbnb) "

    def emptyline(self):
        """ Skips empty line """
        pass

    def do_quit(self, line):
        """ Exits the console """
        return True

    def do_EOF(self, line):
        """ Exits the console """
        return True

    def do_create(self, classname):
        """ Creates a new instance of BaseModel, saves it (to the JSON file) and prints the id """
        if classname == "BaseModel":
            new = BaseModel()
            new.save
            print(new.id)
        elif classname:
            print("** class doesn't exist **")
        else:
            print("** class name missing **")

    def show(self, classname, instid):
        """ Prints the string representation of an instance based on the class name and id """
        # find based on id (stored in instid)
        # print instance
        if len(classname) < 1:
            print("** class name missing **")
        elif classname != "BaseModel":
            print("** class doesn't exist **")
        elif len(id) < 1:
            print("** instance id missing **")
        else:
            # find based on id (stored in instid)
            # if id doesn't exist
                # print("** no instance found **")
            # print instance
            pass

    def destroy(self, classname, instid):
        """ Deletes an instance based on the class name and id (save the change into the JSON file) """
        if len(classname) < 1:
            print("** class name missing **")
        elif classname != "BaseModel":
            print("** class doesn't exist **")
        elif len(id) < 1:
            print("** instance id missing **")
        else:
            # find based on id (stored in instid)
            # if id does not exist
                # print("** no instance found **")
            # delete
            # save
            pass

    def all(self, classname):
        """ Prints all string representation of all instances based or not on the class name """
        if classname != "BaseModel":
            print("** class doesn't exist **")
        else:
            # take everything in __obj of storage file
            # print every instance
            pass

    def update(self, classname, instid, attr, value):
        """ Updates an instance based on the class name and id by adding
        or updating attribute (save the change into the JSON file) """
        if len(classname) < 1:
            print("** class name missing **")
        elif classname != "BaseModel":
            print("** class doesn't exist **")
        elif len(id) < 1:
            print("** instance id missing **")
        elif len(attr) < 1:
            print("** attribute name missing **")
        elif len(value) < 1:
            print("** value missing **")
        else:
            # find based on id (stored in instid)
            # if no id found
                # print("** no instance found **")
            # inst.attr = value
            # save
        pass

if __name__ == '__main__':
        """ Enters console loop """
        HBNBCommand().cmdloop()
