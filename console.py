#!usr/bin/python3
'''Console module for the AirBnB_clone project'''

import cmd

class HBNBCommand(cmd.Cmd):
    prompt = "(hbnb) "

    def do_quit(self, arg):
        '''Quit command to exit program'''
        return True

    def do_EOF(self, arg):
        '''EOF command for exiting the program'''
        print()
        return True

    def emptyline(self):
        '''do nothing when line is empty'''
        pass

if __name__ == '__main__':
    HBNBCommand().cmdloop()