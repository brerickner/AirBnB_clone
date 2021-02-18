#!/usr/bin/python3
""" This module creates the console class """
from models.base_model import BaseModel
import cmd
from models import storage
from models.user import User
from models.city import City
from models.state import State
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class HBNBCommand(cmd.Cmd):
    """ This class creates an interactive console """

    classdict = {'BaseModel': BaseModel,
                 'User': User,
                 'State': State,
                 'City': City,
                 'Amenity': Amenity,
                 'Place': Place,
                 'Review': Review
                 }
    prompt = "(hbnb) "

    def do_BaseModel(self, usrinpt):
        """ Passes all BaseModel input to the correct commands """
        # Split by () before checking match
        # See if it matches up to (
        # Pass the rest of the usrinput into the commands
        # Split input should be [command, inputforcommand]
        splitinput = usrinpt.split("(")
        if splitinput[0] == ".all":
            self.all = self.do_all("BaseModel")
        if splitinput[0] == ".count":
            allInsts = storage.all()
            num = 0
            for key, value in allInsts.items():
                findClass = key.split(".")
                if findClass[0] == "BaseModel":
                    num += 1
            print(num)
        if splitinput[0] == ".show":
            # Would this be easier if we used kwargs instead of splitting?
            updatedinpt = splitinput[1].split(")")
            finalinpt = updatedinpt[0].split("\"")
            info = "BaseModel {}".format(finalinpt[1])
            self.show = self.do_show(info)
        if splitinput[0] == ".destroy":
            updatedinpt = splitinput[1].split(")")
            finalinpt = updatedinpt[0].split("\"")
            info = "BaseModel {}".format(finalinpt[1])
            self.show = self.do_destroy(info)
        if splitinput[0] == ".update":
            updatedinpt = splitinput[1].split(")")
            nocomma = updatedinpt[0].split(", ")
            finalinput = []
            for command in nocomma:
                finalinput.append(command.split("\""))
            commands = "BaseModel "
            for val in finalinput:
                commands += "{} ".format(val[1])
            self.show = self.do_update(commands)

    def do_User(self, usrinpt):
        """ asses all User input to the correct commands """
        splitinput = usrinpt.split("(")
        if splitinput[0] == ".all":
            self.all = self.do_all("User")
        if splitinput[0] == ".show":
            updatedinpt = splitinput[1].split(")")
            finalinpt = updatedinpt[0].split("\"")
            info = "User {}".format(finalinpt[1])
            self.show = self.do_show(info)
        if splitinput[0] == ".destroy":
            updatedinpt = splitinput[1].split(")")
            finalinpt = updatedinpt[0].split("\"")
            info = "User {}".format(finalinpt[1])
            self.show = self.do_destroy(info)
        if splitinput[0] == ".update":
            updatedinpt = splitinput[1].split(")")
            nocomma = updatedinpt[0].split(", ")
            finalinput = []
            for command in nocomma:
                finalinput.append(command.split("\""))
            commands = "User "
            for val in finalinput:
                commands += "{} ".format(val[1])
            self.show = self.do_update(commands)

    def do_State(self, usrinpt):
        """ asses all State input to the correct commands """
        splitinput = usrinpt.split("(")
        if splitinput[0] == ".all":
            self.all = self.do_all("State")
        if splitinput[0] == ".show":
            updatedinpt = splitinput[1].split(")")
            finalinpt = updatedinpt[0].split("\"")
            info = "State {}".format(finalinpt[1])
            self.show = self.do_show(info)
        if splitinput[0] == ".destroy":
            updatedinpt = splitinput[1].split(")")
            finalinpt = updatedinpt[0].split("\"")
            info = "State {}".format(finalinpt[1])
            self.show = self.do_destroy(info)
        if splitinput[0] == ".update":
            updatedinpt = splitinput[1].split(")")
            nocomma = updatedinpt[0].split(", ")
            finalinput = []
            for command in nocomma:
                finalinput.append(command.split("\""))
            commands = "State "
            for val in finalinput:
                commands += "{} ".format(val[1])
            self.show = self.do_update(commands)

    def do_City(self, usrinpt):
        """ asses all City input to the correct commands """
        splitinput = usrinpt.split("(")
        if splitinput[0] == ".all":
            self.all = self.do_all("City")
        if splitinput[0] == ".show":
            updatedinpt = splitinput[1].split(")")
            finalinpt = updatedinpt[0].split("\"")
            info = "City {}".format(finalinpt[1])
            self.show = self.do_show(info)
        if splitinput[0] == ".destroy":
            updatedinpt = splitinput[1].split(")")
            finalinpt = updatedinpt[0].split("\"")
            info = "City {}".format(finalinpt[1])
            self.show = self.do_destroy(info)
        if splitinput[0] == ".update":
            updatedinpt = splitinput[1].split(")")
            nocomma = updatedinpt[0].split(", ")
            finalinput = []
            for command in nocomma:
                finalinput.append(command.split("\""))
            commands = "City "
            for val in finalinput:
                commands += "{} ".format(val[1])
            self.show = self.do_update(commands)

    def do_Amenity(self, usrinpt):
        """ asses all Amenity input to the correct commands """
        splitinput = usrinpt.split("(")
        if splitinput[0] == ".all":
            self.all = self.do_all("Amenity")
        if splitinput[0] == ".show":
            updatedinpt = splitinput[1].split(")")
            finalinpt = updatedinpt[0].split("\"")
            info = "Amenity {}".format(finalinpt[1])
            self.show = self.do_show(info)
        if splitinput[0] == ".destroy":
            updatedinpt = splitinput[1].split(")")
            finalinpt = updatedinpt[0].split("\"")
            info = "Amenity {}".format(finalinpt[1])
            self.show = self.do_destroy(info)
        if splitinput[0] == ".update":
            updatedinpt = splitinput[1].split(")")
            nocomma = updatedinpt[0].split(", ")
            finalinput = []
            for command in nocomma:
                finalinput.append(command.split("\""))
            commands = "Amenity "
            for val in finalinput:
                commands += "{} ".format(val[1])
            self.show = self.do_update(commands)

    def do_Place(self, usrinpt):
        """ asses all Place input to the correct commands """
        splitinput = usrinpt.split("(")
        if splitinput[0] == ".all":
            self.all = self.do_all("Place")
        if splitinput[0] == ".show":
            updatedinpt = splitinput[1].split(")")
            finalinpt = updatedinpt[0].split("\"")
            info = "Place {}".format(finalinpt[1])
            self.show = self.do_show(info)
        if splitinput[0] == ".destroy":
            updatedinpt = splitinput[1].split(")")
            finalinpt = updatedinpt[0].split("\"")
            info = "Place {}".format(finalinpt[1])
            self.show = self.do_destroy(info)
        if splitinput[0] == ".update":
            updatedinpt = splitinput[1].split(")")
            nocomma = updatedinpt[0].split(", ")
            finalinput = []
            for command in nocomma:
                finalinput.append(command.split("\""))
            commands = "Place "
            for val in finalinput:
                commands += "{} ".format(val[1])
            self.show = self.do_update(commands)

    def do_Review(self, usrinpt):
        """ asses all Review input to the correct commands """
        splitinput = usrinpt.split("(")
        if splitinput[0] == ".all":
            self.all = self.do_all("Review")
        if splitinput[0] == ".show":
            updatedinpt = splitinput[1].split(")")
            finalinpt = updatedinpt[0].split("\"")
            info = "Review {}".format(finalinpt[1])
            self.show = self.do_show(info)
        if splitinput[0] == ".destroy":
            updatedinpt = splitinput[1].split(")")
            finalinpt = updatedinpt[0].split("\"")
            info = "Review {}".format(finalinpt[1])
            self.show = self.do_destroy(info)
        if splitinput[0] == ".update":
            updatedinpt = splitinput[1].split(")")
            nocomma = updatedinpt[0].split(", ")
            finalinput = []
            for command in nocomma:
                finalinput.append(command.split("\""))
            commands = "Review "
            for val in finalinput:
                commands += "{} ".format(val[1])
            self.show = self.do_update(commands)

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
        """ Creates a new instance of BaseModel, saves
        it (to the JSON file) and prints the id """
        check = 0
        for key, value in self.classdict.items():
            if classname == key:
                new = value()
                new.save()
                print(new.id)
                check = 1
        if classname and check == 0:
            print("** class doesn't exist **")
        elif check == 0:
            print("** class name missing **")

    def do_show(self, usrinpt):
        """ Prints the string representation of an
        instance based on the class name and id """
        if len(usrinpt) < 1:
            print("** class name missing **")
        else:
            inargs = usrinpt.split()
            # inargs = [class, id]
            if inargs[0] not in self.classdict.keys():
                print("** class doesn't exist **")
            elif len(inargs) < 2:
                print("** instance id missing **")
            else:
                # find based on id (stored in instid)
                allInsts = storage.all()
                check = 0
                collectvalues = []
                for key, value in allInsts.items():
                    if key == "{}.{}".format(inargs[0], inargs[1]):
                        collectvalues.append(str(value))
                        print(value)
                        check = 1
                        break
                if check == 0:
                    print("** no instance found **")

    def do_destroy(self, usrinpt):
        """ Deletes an instance based on the class
        name and id (save the change into the JSON file) """
        # inargs[0] = classname, inargs[1] = instid
        if len(usrinpt) < 1:
            print("** class name missing **")
        else:
            inargs = usrinpt.split()
            if inargs[0] not in self.classdict.keys():
                print("** class doesn't exist **")
            elif len(inargs) < 2:
                print("** instance id missing **")
            else:
                allInsts = storage.all()
                check = 0
                for key in allInsts:
                    if key == "{}.{}".format(inargs[0], inargs[1]):
                        del allInsts[key]
                        storage.save()
                        check = 1
                        break
                if check == 0:
                    print("** no instance found **")

    def do_all(self, usrinpt):
        """ Prints all string representation of
        all instances based or not on the class name """
        clsList = []
        check = 0
        if not usrinpt:
            allInsts = storage.all()
            for key, value in allInsts.items():
                print(value)
            check = 1
        if usrinpt in self.classdict.keys():
            allInsts = storage.all()
            for key, value in allInsts.items():
                findClass = key.split(".")
                if usrinpt == findClass[0]:
                    # clsFound = str(key) + str(value)
                    clsList.append(str(value))
            print(clsList)
            check = 1
        elif check == 0:
            print("** class doesn't exist **")

    def do_update(self, usrinpt):
        """ Updates an instance based on the class name and id by adding
        or updating attribute (save the change into the JSON file)
        format: [classname, instid, attr, value]"""
        # inargs = [classname, instid, attr, value]
        inargs = usrinpt.split(" ", 3)
        if len(inargs) < 1:
            print("** class name missing **")
        elif inargs[0] not in self.classdict.keys():
            print("** class doesn't exist **")
        elif len(inargs) < 2:
            print("** instance id missing **")
        elif len(inargs) < 3:
            print("** attribute name missing **")
        elif len(inargs) < 4:
            print("** value missing **")
        else:
            allInsts = storage.all()
            check = 0
            collectvalues = []
            if inargs[2] == "id" or inargs[2] == "created_at":
                return
            if inargs[2] == "updated_at":
                return
            for key, value in allInsts.items():
                if key == "{}.{}".format(inargs[0], inargs[1]):
                    collectvalues.append(value)
                    try:
                        setattr(value, inargs[2], int(inargs[3]))
                        check = 1
                    except:
                        try:
                            setattr(value, inargs[2], float(inargs[3]))
                            check = 1
                        except:
                            try:
                                arg3String = str(inargs[3]).split('\"')
                                if len(arg3String) > 0:
                                    setattr(value, inargs[2], arg3String[1])
                                    # value.inargs[2] = inargs[3]
                                    check = 1
                                    break
                            except:
                                setattr(value, inargs[2], arg3String[0])
                                check = 1
            if check == 0:
                print("** no instance found **")
if __name__ == '__main__':
        """ Enters console loop """
        HBNBCommand().cmdloop()
