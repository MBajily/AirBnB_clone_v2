#!/usr/bin/python3
"""
Contains the TestDBStorageDocs and TestDBStorage classes
"""
from datetime import datetime
import inspect
import models
from models.engine import db_storage
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User
from models.amenity import Amenity
from models.city import City
import json
import os
import pycodestyle
import unittest


DBStorage = db_storage.DBStorage

storage_t = os.getenv("HBNB_TYPE_STORAGE")
classes = {
    "Amenity": Amenity,
    "City": City,
    "Place": Place,
    "Review": Review,
    "State": State,
    "User": User
}


class TestDBStorageDocs(unittest.TestCase):
    """Test case to check the documentation and style of the DBStorage class"""

    @classmethod
    def setUpClass(cls):
        """Set up for the doc tests"""
        cls.dbs_f = inspect.getmembers(DBStorage, inspect.isfunction)

    def test_pep8_conformance_test_db_storage(self):
        """Test that tests/test_models/test_db_storage.py conforms to PEP8."""
        pep8style = pycodestyle.StyleGuide(quiet=True)
        theResult = pep8style.check_files(['tests/test_models/test_engine/\
test_db_storage.py'])
        self.assertEqual(theResult.total_errors, 0,
                         "Found code style errors (and warnings).")

    def test_pep8_conformance_db_storage(self):
        """Test that models/engine/db_storage.py conforms to PEP8 style."""
        pep8style = pycodestyle.StyleGuide(quiet=True)
        theResult = pep8style.check_files(['models/engine/db_storage.py'])
        self.assertEqual(theResult.total_errors, 0,
                         "Found code style errors (and warnings).")


class TestDBStorageDocs(unittest.TestCase):
    """Test case to check the documentation and style of the DBStorage class"""
    @classmethod
    def setUpClass(cls):
        """Set up for the doc tests"""
        cls.dbs_f = inspect.getmembers(DBStorage, inspect.isfunction)

    def test_pep8_conformance_db_storage(self):
        """Test that models/engine/db_storage.py conforms to PEP8 style."""
        pep8style = pycodestyle.StyleGuide(quiet=True)
        theResult = pep8style.check_files(['models/engine/db_storage.py'])
        self.assertEqual(theResult.total_errors, 0,
                         "Found code style errors (and warnings).")

    def test_pep8_conformance_test_db_storage(self):
        """Test that tests/test_models/test_db_storage.py conforms to PEP8."""
        pep8style = pycodestyle.StyleGuide(quiet=True)
        theResult = pep8style.check_files(['tests/test_models/test_engine/\
test_db_storage.py'])
        self.assertEqual(theResult.total_errors, 0,
                         "Found code style errors (and warnings).")

    def test_db_storage_class_docstring(self):
        """Test the docstring of the DBStorage class"""
        self.assertIsNot(DBStorage.__doc__, None,
                         "DBStorage class needs a docstring")
        self.assertTrue(len(DBStorage.__doc__) >= 1,
                        "DBStorage class needs a docstring")

    def test_db_storage_module_docstring(self):
        """Test the docstring of the db_storage.py module"""
        self.assertIsNot(db_storage.__doc__, None,
                         "db_storage.py needs a docstring")
        self.assertTrue(len(db_storage.__doc__) >= 1,
                        "db_storage.py needs a docstring")

    def test_dbs_func_docstrings(self):
        """Test the presence of docstrings in DBStorage methods"""
        for func in self.dbs_f:
            self.assertIsNot(func[1].__doc__, None,
                             "{:s} method needs a docstring".format(func[0]))
            self.assertTrue(len(func[1].__doc__) >= 1,
                            "{:s} method needs a docstring".format(func[0]))


class TestFileStorage(unittest.TestCase):
    """Test case for the FileStorage class"""

    @unittest.skipIf(storage_t != 'db', "not testing db storage")
    def test_new(self):
        """Test if new method adds an object to the database"""
        pass

    @unittest.skipIf(storage_t != 'db', "not testing db storage")
    def test_save(self):
        """Test if save method properly saves objects to file.json"""
        pass
    
    @unittest.skipIf(storage_t != 'db', "not testing db storage")
    def test_all_returns_dict(self):
        """Test if all method returns a dictionary"""
        self.assertIs(type(models.storage.all()), dict)

    @unittest.skipIf(storage_t != 'db', "not testing db storage")
    def test_all_no_class(self):
        """Test if all method returns all rows when no class is passed"""
        pass
