#!/usr/bin/python3
from models.base_model import BaseModel

import cmd
from models import storage

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
            new.save()
            print(new.id)
        elif classname:
            print("** class doesn't exist **")
        else:
            print("** class name missing **")

    def do_show(self, usrinpt):
        """ Prints the string representation of an instance based on the class name and id """
        if len(usrinpt) < 1:
            print("** class name missing **")
        else:
            inargs = usrinpt.split()
            # inargs = [class, id]
            if inargs[0] != "BaseModel":
               print("** class doesn't exist **")
            elif len(inargs) < 2:
                print("** instance id missing **")
            else:
                # find based on id (stored in instid)
                allInsts = storage.all()
                check = 0
                collectKeys =[]
                for key,value in allInsts.items():
                    # ERROR: THIS NEEDS TO PRINT IN STRING FORMAT
                    if key == "{}.{}".format(inargs[0], inargs[1]):
                        collectKeys.append(str(value))
                        print(value)
                        check = 1
                        break
                if check == 0:
                    print("** no instance found **")

    def do_destroy(self, usrinpt):
        """ Deletes an instance based on the class name and id (save the change into the JSON file) """
        # inargs[0] = classname, inargs[1] = instid
        inargs = usrinpt.split()
        if not inargs:
            print("** class name missing **")
        elif inargs[0] != "BaseModel":
            print("** class doesn't exist **")
        elif len(inargs) < 2:
            print("** instance id missing **")
        else:
            allInsts = storage.all()
            check = 0
            for key in allInsts:
                if key == "{}.{}".format(inargs[0], inargs[1]):
                    del allInsts[key]
                    storage.save
                    check = 1
                    break
                if check == 0:
                    print("** no instance found **")

    def do_all(self, usrinpt):
        """ Prints all string representation of all instances based or not on the class name """
        clsList = []
        if not usrinpt and usrinpt != "BaseModel":
            print("** class doesn't exist **")
        else:
            allInsts = storage.all()
            for key, value in allInsts.items():
                findClass = key.split(".")
                if usrinpt == findClass[0]:
                   # clsFound = str(key) + str(value) 
                    clsList.append(str(value))
            print(clsList)


    def do_update(self, usrinpt):
        """ Updates an instance based on the class name and id by adding
        #or updating attribute (save the change into the JSON file) """
        #inargs = [classname, instid, attr, value]
        inargs = usrinpt.split()
        if len(inargs) < 1:
            print("** class name missing **")
        elif inargs[0] != "BaseModel":
            print("** class doesn't exist **")
        elif len(inargs) < 2:
            print("** instance id missing **")
        elif len(inargs) < 3:
            print("** attribute name missing **")
        elif len(inargs) < 4:
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
