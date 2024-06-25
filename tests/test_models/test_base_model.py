#!/usr/bin/python3
"""
Unit tests for the BaseModel class
"""
from models.base_model import BaseModel
import unittest
import datetime
from uuid import UUID
import json
import os
import pycodestyle
import inspect


class TestBaseModel(unittest.TestCase):
    """
    Test class for the BaseModel class
    """

    def __init__(self, *args, **kwargs):
        """
        Constructor for TestBaseModel
        """
        super().__init__(*args, **kwargs)
        self.class_name = 'BaseModel'
        self.base_model = BaseModel

    def test_pycodestyle(self):
        """
        Test the PEP 8 style of base_model.py
        """
        pycodestyle_checker = pycodestyle.StyleGuide(quiet=True)
        result = pycodestyle_checker.check_files(['models/base_model.py'])
        self.assertEqual(result.total_errors, 0, "Found code style errors.")

    def setUp(self):
        """
        Set up method for each test case
        """
        pass

    def tearDown(self):
        """
        Tear down method for each test case
        """
        try:
            os.remove('file.json')
        except:
            pass

    def test_default(self):
        """
        Test the default constructor
        """
        instance = self.base_model()
        self.assertEqual(type(instance), self.base_model)

    def test_kwargs(self):
        """
        Test the constructor with **kwargs
        """
        instance = self.base_model()
        copy = instance.to_dict()
        new_instance = BaseModel(**copy)
        self.assertFalse(new_instance is instance)

    def test_kwargs_int(self):
        """
        Test the constructor with invalid kwargs (int)
        """
        instance = self.base_model()
        copy = instance.to_dict()
        copy.update({1: 2})
        with self.assertRaises(TypeError):
            new_instance = BaseModel(**copy)

    def test_save(self):
        """
        Test the save method
        """
        instance = self.base_model()
        instance.save()
        key = self.class_name + "." + instance.id
        with open('file.json', 'r') as f:
            data = json.load(f)
            self.assertEqual(data[key], instance.to_dict())

    def test_str(self):
        """
        Test the __str__ method
        """
        instance = self.base_model()
        self.assertEqual(str(instance), '[{}] ({}) {}'.format(
            self.class_name, instance.id, instance.__dict__))

    def test_todict(self):
        """
        Test the to_dict method
        """
        instance = self.base_model()
        dict_data = instance.to_dict()
        self.assertEqual(instance.to_dict(), dict_data)

    def test_kwargs_none(self):
        """
        Test the constructor with None as kwargs
        """
        kwargs = {None: None}
        with self.assertRaises(TypeError):
            instance = self.base_model(**kwargs)

    def test_id(self):
        """
        Test the id attribute
        """
        instance = self.base_model()
        self.assertEqual(type(instance.id), str)

    def test_created_at(self):
        """
        Test the created_at attribute
        """
        instance = self.base_model()
        self.assertEqual(type(instance.created_at), datetime.datetime)

    def test_updated_at(self):
        """
        Test the updated_at attribute
        """
        instance = self.base_model()
        self.assertEqual(type(instance.updated_at), datetime.datetime)
        dict_data = instance.to_dict()
        new_instance = BaseModel(**dict_data)
        self.assertFalse(new_instance.created_at == new_instance.updated_at)

    def test_uuid(self):
        """
        Test the uniqueness of UUIDs
        """
        instance1 = self.base_model()
        instance2 = self.base_model()
        instance3 = self.base_model()
        instances_list = [instance1, instance2, instance3]
        for instance in instances_list:
            instance_uuid = instance.id
            with self.subTest(uuid=instance_uuid):
                self.assertIs(type(instance_uuid), str)
        self.assertNotEqual(instance1.id, instance2.id)
        self.assertNotEqual(instance1.id, instance3.id)
        self.assertNotEqual(instance2.id, instance3.id)

    def test_str_method(self):
        """
        Test the return value of the __str__ method
        """
        instance = self.base_model()
        string_output = "[BaseModel] ({}) {}".format(
            instance.id, instance.__dict__)
        self.assertEqual(string_output, str(instance))


class TestCodeFormat(unittest.TestCase):
    """
    Test class to check the code format using PEP 8
    """

    def test_pycodestyle(self):
        """
        Test the PEP 8 style of base_model.py
        """
        pycodestyle_checker = pycodestyle.StyleGuide(quiet=True)
        result = pycodestyle_checker.check_files(['models/base_model.py'])
        self.assertEqual(result.total_errors, 0, "Found codestyle errors.")

class TestDocstrings(unittest.TestCase):
    """
    Test class to check the docstrings
    """

    @classmethod
    def setUpClass(cls):
        """
        Set up class method
        """
        cls.obj_members(BaseModel, inspect.isfunction)


class TestBaseModel(unittest.TestCase):
    """
    Test class for the BaseModel class
    """

    @classmethod
    def setUpClass(cls):
        """
        Set up class method
        """
        cls.base = BaseModel()
        cls.base.name = "Kev"
        cls.base.num = 20

    @classmethod
    def tearDownClass(cls):
        """
        Tear down class method
        """
        del cls.base

    def tearDown(self):
        """
        Tear down method for each test case
        """
        try:
            os.remove("file.json")
        except Exception:
            pass

    def test_pep8(self):
        """
        Test for PEP 8 style
        """
        style = pep8.StyleGuide(quiet=True)
        p = style.check_files(['models/base_model.py'])
        self.assertEqual(p.total_errors, 0, "Fix PEP 8 style")

    def test_docstrings(self):
        """
        Test for docstrings
        """
        self.assertIsNotNone(BaseModel.__doc__)
        self.assertIsNotNone(BaseModel.__init__.__doc__)
        self.assertIsNotNone(BaseModel.__str__.__doc__)
        self.assertIsNotNone(BaseModel.save.__doc__)
        self.assertIsNotNone(BaseModel.to_dict.__doc__)

    def test_methods(self):
        """
        Test if BaseModel has required methods
        """
        self.assertTrue(hasattr(BaseModel, "__init__"))
        self.assertTrue(hasattr(BaseModel, "save"))
        self.assertTrue(hasattr(BaseModel, "to_dict"))

    def test_init(self):
        """
        Test if base is an instance of BaseModel
        """
        self.assertTrue(isinstance(self.base, BaseModel))

    def test_save(self):
        """
        Test if save method works
        """
        self.base.save()
        self.assertNotEqual(self.base.created_at, self.base.updated_at)

    def test_to_dict(self):
        """
        Test if to_dict method works
        """
        base_dict = self.base.to_dict()
        self.assertEqual(self.base.__class__.__name__, 'BaseModel')
        self.assertIsInstance(base_dict['created_at'], str)
        self.assertIsInstance(base_dict['updated_at'], str)


if __name__ == "__main__":
    unittest.main()

if __name__ == "__main__":
    unittest.main()
