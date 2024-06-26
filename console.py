#!/usr/bin/python3
"""Console Module"""
import cmd
import sys
from models.base_model import BaseModel
from models.__init__ import storage
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review


class HBNBCommand(cmd.Cmd):
    """Contains the functionality for the HBNB console"""

    # Determines prompt for interactive/non-interactive modes
    prompt = '(hbnb) ' if sys.__stdin__.isatty() else ''

    classes = {
        'BaseModel': BaseModel, 'User': User, 'Place': Place,
        'State': State, 'City': City, 'Amenity': Amenity,
        'Review': Review
    }
    dot_commands = ['all', 'count', 'show', 'destroy', 'update']
    types = {
        'number_rooms': int, 'number_bathrooms': int,
        'max_guest': int, 'price_by_night': int,
        'latitude': float, 'longitude': float
    }

    def preloop(self):
        """Prints if isatty is false"""
        if not sys.__stdin__.isatty():
            print('(hbnb)')

    def precmd(self, line):
        """Reformat command line for advanced command syntax.

        Usage: <class name>.<command>([<id> [<*args> or <**kwargs>]])
        (Brackets denote optional fields in usage example.)
        """
        cmd_name = cls_name = obj_id = obj_args = ''  # Initialize line elements

        # Scan for general formatting - i.e., '.', '(', ')'
        if not ('.' in line and '(' in line and ')' in line):
            return line

        try:  # Parse line left to right
            parsed_line = line[:]  # Parsed line

            # Isolate <class name>
            cls_name = parsed_line[:parsed_line.find('.')]

            # Isolate and validate <command>
            cmd_name = parsed_line[parsed_line.find('.') + 1:parsed_line.find('(')]
            if cmd_name not in HBNBCommand.dot_commands:
                raise Exception

            # If parentheses contain arguments, parse them
            parsed_line = parsed_line[parsed_line.find('(') + 1:parsed_line.find(')')]
            if parsed_line:
                # Partition args: (<id>, [<delim>], [<*args>])
                parsed_line = parsed_line.partition(', ')  # parsed_line converted to tuple

                # Isolate obj_id, stripping quotes
                obj_id = parsed_line[0].replace('\"', '')
                # Possible bug here:
                # Empty quotes register as empty obj_id when replaced

                # If arguments exist beyond obj_id
                parsed_line = parsed_line[2].strip()  # parsed_line is now str
                if parsed_line:
                    # Check for *args or **kwargs
                    if parsed_line[0] == '{' and parsed_line[-1] == '}' and type(eval(parsed_line)) is dict:
                        obj_args = parsed_line
                    else:
                        obj_args = parsed_line.replace(',', '')
                        # obj_args = obj_args.replace('\"', '')
            line = ' '.join([cmd_name, cls_name, obj_id, obj_args])

        except Exception as e:
            pass
        finally:
            return line

    def postcmd(self, stop, line):
        """Prints if isatty is false"""
        if not sys.__stdin__.isatty():
            print('(hbnb) ', end='')
        return stop

    def do_quit(self, args):
        """Method to exit the HBNB console"""
        exit()

    def help_quit(self):
        """Prints the help documentation for quit"""
        print("Exits the program with formatting\n")

    def do_EOF(self, args):
        """Handles EOF to exit program"""
        print()
        exit()

    def help_EOF(self):
        """Prints the help documentation for EOF"""
        print("Exits the program without formatting\n")

    def emptyline(self):
        """Overrides the emptyline method of CMD"""
        pass

    def do_create(self, args):
        """Create an object of any class"""
        try:
            if not args:
                raise SyntaxError()
            arg_list = args.split(" ")
            kwargs = {}
            for arg in arg_list[1:]:
                arg_split = arg.split("=")
                arg_split[1] = eval(arg_split[1])
                if type(arg_split[1]) is str:
                    arg_split[1] = arg_split[1].replace("_", " ").replace('"', '\\"')
                kwargs[arg_split[0]] = arg_split[1]
        except SyntaxError:
            print("** class name missing **")
        except NameError:
            print("** class doesn't exist **")
        new_instance = HBNBCommand.classes[arg_list[0]](**kwargs)
        new_instance.save()
        print(new_instance.id)

    def help_create(self):
        """Help information for the create method"""
        print("Creates an instance of a class")
        print("[Usage]: create <className>\n")

    def do_show(self, args):
        """Method to show an individual object"""
        new_args = args.partition(" ")
        class_name = new_args[0]
        instance_id = new_args[2]

        # Guard against trailing args
        if instance_id and ' ' in instance_id:
            instance_id = instance_id.partition(' ')[0]

        if not class_name:
            print("** class name missing **")
            return

        if class_name not in HBNBCommand.classes:
            print("** class doesn't exist **")
            return

        if not instance_id:
            print("** instance id missing **")
            return

        key = class_name + "." + instance_id
        try:
            print(storage._FileStorage__objects[key])
        except KeyError:
            print("** no instance found **")

    def help_show(self):
        """Help information for the show command"""
        print("Shows an individual instance of a class")
        print("[Usage]: show <className> <instanceId>\n")

    def do_destroy(self, args):
        """Method to delete an object"""
        new_args = args.partition(" ")
        class_name = new_args[0]
        instance_id = new_args[2]

        # Guard against trailing args
        if instance_id and ' ' in instance_id:
            instance_id = instance_id.partition(' ')[0]

        if not class_name:
            print("** class name missing **")
            return

        if class_name not in HBNBCommand.classes:
            print("** class doesn't exist **")
            return

        if not instance_id:
            print("** instance id missing **")
            return

        key = class_name + "." + instance_id
        try:
            del storage._FileStorage__objects[key]
            storage.save()
        except KeyError:
            print("** no instance found **")

    def help_destroy(self):
        """Help information for the destroy command"""
        print("Deletes an instance of a class")
        print("[Usage]: destroy <className> <instanceId>\n")

    def do_all(self, args):
        """Method to display all objects"""
        new_args = args.partition(" ")
        class_name = new_args[0]

        if not class_name:
            objects = storage.all()
            print([str(obj) for obj in objects.values()])
            return

        if class_name not in HBNBCommand.classes:
            print("** class doesn't exist **")
            return

        objects = storage.all(class_name)
        print([str(obj) for obj in objects.values()])

    def help_all(self):
        """Help information for the all command"""
        print("Displays all instances or instances of a specific class")
        print("[Usage]: all or all <className>\n")

    def do_update(self, args):
        """Method to update an object"""
        new_args = args.split(" ")
        class_name = new_args[0]

        if not class_name:
            print("** class name missing **")
            return

        if class_name not in HBNBCommand.classes:
            print("** class doesn't exist **")
            return

        if len(new_args) < 2:
            print("** instance id missing **")
            return

        instance_id = new_args[1]

        key = class_name + "." + instance_id

        if key not in storage._FileStorage__objects:
            print("** no instance found **")
            return

        if len(new_args) < 3:
            print("** attribute name missing **")
            return

        if len(new_args) < 4:
            print("** value missing **")
            return

        attr_name = new_args[2]
        attr_value = new_args[3]

        obj = storage._FileStorage__objects[key]
        setattr(obj, attr_name, attr_value)
        storage.save()

    def help_update(self):
        """Help information for the update command"""
        print("Updates an instance attribute of a class")
        print("[Usage]: update <className> <instanceId> <attributeName> <attributeValue>\n")

if __name__ == "__main__":
    HBNBCommand().cmdloop()
