#!/usr/bin/python3
"""Console module."""
import cmd
import shlex
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.place import Place
from models.amenity import Amenity
from models.review import Review
from models import storage

classes = {"BaseModel": BaseModel, "User": User, "State": State,
           "City": City, "Place": Place, "Amenity": Amenity, "Review": Review}


class HBNBCommand(cmd.Cmd):
    """Command Line Interpreter"""

    prompt = "(hbnb) "

    def do_EOF(self, line):
        """EOF command to exit the program"""
        return True

    def emptyline(self):
        """Handles empty line input"""
        pass

    def do_quit(self, line):
        """Quit command to exit the program"""
        return True

    def do_create(self, line):
        """Creates a new instance of BaseModel"""
        if not line:
            print("** class name missing **")
            return

        args = shlex.split(line)
        class_name = args[0]

        if class_name not in classes:
            print("** class doesn't exist **")
            return

        new_instance = classes[class_name]()
        new_instance.save()
        print(new_instance.id)

    def do_show(self, line):
        """Prints the string representation of an instance"""
        if not line:
            print("** class name missing **")
            return

        args = shlex.split(line)
        class_name = args[0]

        if class_name not in classes:
            print("** class doesn't exist **")
            return

        if len(args) < 2:
            print("** instance id missing **")
            return

        instance_id = args[1]
        key = "{}.{}".format(class_name, instance_id)

        all_objs = storage.all()

        if key not in all_objs:
            print("** no instance found **")
        else:
            print(all_objs[key])

    def do_destroy(self, line):
        """Deletes an instance based on the class name and id"""
        if not line:
            print("** class name missing **")
            return

        args = shlex.split(line)
        class_name = args[0]

        if class_name not in classes:
            print("** class doesn't exist **")
            return

        if len(args) < 2:
            print("** instance id missing **")
            return

        instance_id = args[1]
        key = "{}.{}".format(class_name, instance_id)

        all_objs = storage.all()

        if key not in all_objs:
            print("** no instance found **")
            return

        del all_objs[key]
        storage.save()

    def do_all(self, line):
        """Prints all string representations of all instances"""
        args = shlex.split(line)
        if not args or args[0] not in classes:
            print([str(value) for key, value in storage.all().items()])
        else:
            print([str(value) for key, value in storage.all().items()
                   if args[0] == key.split('.')[0]])

    def do_update(self, line):
        """Updates an instance based on the class name and id or with a dictionary"""
        if not line:
            print("** class name missing **")
            return

        args = shlex.split(line)
        class_name = args[0]

        if class_name not in classes:
            print("** class doesn't exist **")
            return

        if len(args) < 2:
            print("** instance id missing **")
            return

        instance_id = args[1]
        key = "{}.{}".format(class_name, instance_id)

        all_objs = storage.all()

        if key not in all_objs:
            print("** no instance found **")
            return

        if len(args) < 3:
            print("** attribute name missing **")
            return

        if len(args) < 4:
            print("** value missing **")
            return

        attribute_name = args[2]
        attribute_value = args[3]

        if attribute_name in dir(all_objs[key]):
            attribute_value = type(getattr(all_objs[key], attribute_name))(attribute_value)

        setattr(all_objs[key], attribute_name, attribute_value)
        storage.save()

    def do_count(self, line):
        """Counts the number of instances of a class"""
        args = shlex.split(line)
        if not args or args[0] not in classes:
            print(len(storage.all()))
        else:
            print(len([value for key, value in storage.all().items()
                       if args[0] == key.split('.')[0]]))

if __name__ == '__main__':
    HBNBCommand().cmdloop()
