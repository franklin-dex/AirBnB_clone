#!usr/bin/python3
'''Console module for the AirBnB_clone project'''

import cmd
from models.base_model import BaseModel
from models.__init__ import storage

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

    def do_create(self, arg):
        '''create new instance of basemodel, save it to a JSON file'''
        if not arg:
            print("** class name missing **")
            return
        try:
            new_instance = eval(arg)()
            new_instance.save()
            print(new_instance.id)
        except NameError:
            print("** class do not exist **")

    def do_show(self, arg):
        '''print srting representation of insatnce based on the class name and id'''
        args = arg.slpit()
        if not args or args[0] == "":
            print("** class name is missing **")
            return
        try:
            class_name = args[0]
            instance_id = args[1]
            key = "{}.{}".format(class_name, instance_id)
            obj = storage.all().get(key)
            if obj is None:
                print("** no instance found **")
            else:
                print(obj)
        except IndexError:
            print("** instance id missing **")
        except NameError:
            print('** class do not exist **')
def do_destroy(self, arg):
    '''deletes an instance based on the class name and id'''
    args =arg.split()
    if not args or args[0] == "":
        print("** class name missing **")
        return
    try:
        class_name = args[0]
        instance_id = args[1]
        key = "{}.{}".format(class_name, instance_id)
        obj = storage.all().get(key)
        if obj is None:
            print("** no instance found **")
        else:
            del storage.all()[key]
            storage.save()
    except IndexError:
        print('** instance id missing **')
    except NameError:
        print("** class do not exist **")

def do_all(self, args):
        """ Shows all objects, or all objects of a class"""
        print_list = []

        if args:
            args = args.split(' ')[0]  # remove possible trailing args
            if args not in HBNBCommand.classes:
                print("** class doesn't exist **")
                return
            for k, v in storage.all(HBNBCommand.classes[args]).items():
                print_list.append(str(v))
        else:
            for k, v in storage.all().items():
                print_list.append(str(v))
        print(print_list)

def do_update(self, arg):
    '''updates an instance bsed on the class name and id by adding or updating an attribute'''
    args = arg.split()
    if not args or agrs[0] == "":
        print("** class name missing **")
        return
    try:
        class_name =args[0]
        instance_id = args[1]
        key = "{}.{}".format(class_name, instance_id)
        obj = storage.all().get(key)
        if obj is None:
            print("** No instance found **")
            return
        if len(args) < 3:
            print("** attribute name missing **")
            return
        attr_name = args[2]
        if len(arg) < 4:
            print("** value missing **")
            return
        attr_value = args[5]
        setattr(obj, attr_name, attr_value)
        obj.save()
    except IndexError:
        print("** instance missing **")
    except NameError:
        print("** class do not exist **")
    
if __name__ == '__main__':
    HBNBCommand().cmdloop()
