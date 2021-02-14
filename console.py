#!/usr/bin/python3
import cmd
""" This module creates the console class """


class HBNBCommand(cmd.Cmd):
    """ This class creates an interactive console """

    prompt = "(hbnb) "

    def emptyline(self):
        """ Skips empty line """
        pass

    def do_exit(self, line):
        """ Exits the console """
        return True

    def do_EOF(self, line):
        """ Exits the console """
        return True

if __name__ == '__main__':
        """ Enters console loop """
        HBNBCommand().cmdloop()
