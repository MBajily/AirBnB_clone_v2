#!/usr/bin/python3
"""This is the file storage class for AirBnB clone project"""
import json
import shlex


class FileStorage:
    """FileStorage model
    Attributes:
        __file_path: path to the JSON file
        __objects: objects will be stored
    """
    __objects = {}
    __file_path = "file.json"


    def all(self, cls=None):
        """returns all dictionary
        Return:
            returns a dictionary of __object
        """
        result = {}

        if cls:
            dictionary = self.__objects

            for key in dictionary:
                part = key.replace('.', ' ')
                part = shlex.split(part)

                if (part[0] == cls.__name__):
                    result[key] = self.__objects[key]

            return (result)

        else:
            return self.__objects


    def new(self, obj):
        """add new object
        Args:
            obj: given object
        """
        if obj:
            key = "{}.{}".format(type(obj).__name__, obj.id)
            self.__objects[key] = obj


    def reload(self):
        """serialize to JSON file path
        """
        try:
            with open(self.__file_path, 'r', encoding="UTF-8") as f:
                for key, value in (json.load(f)).items():
                    value = eval(value["__class__"])(**value)
                    self.__objects[key] = value

        except FileNotFoundError:
            pass


    def delete(self, obj=None):
        """ delete an element
        """
        if obj:
            key = "{}.{}".format(type(obj).__name__, obj.id)
            del self.__objects[key]

    def save(self):
        """Save the changes
        """
        saveDict = {}

        for key, value in self.__objects.items():
            saveDict[key] = value.to_dict()

        with open(self.__file_path, 'w', encoding="UTF-8") as f:
            json.dump(saveDict, f)

    def close(self):
        """ calls reload()
        """
        self.reload()
