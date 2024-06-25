#!/usr/bin/python3
""" """
from tests.test_models.test_base_model import test_basemodel
from models.amenity import Amenity
from models.base_model import BaseModel
from datetime import datetime
from unittest.mock import patch
from time import sleep
from os import getenv
import pycodestyle
import inspect
import unittest

storage_type = getenv("HBNB_TYPE_STORAGE")


class TestAmenityModel(test_basemodel):
    """ """

    def __init__(self, *args, **kwargs):
        """ """
        super().__init__(*args, **kwargs)
        self.name = "Amenity"
        self.value = Amenity

    def test_name(self):
        """ """
        new_amenity = self.value()
        self.assertEqual(type(new_amenity.name), str)


class TestPEP8(unittest.TestCase):
    """Test PEP8 style"""
    def test_pep8_style(self):
        """Test PEP8 style"""
        pep8style = pycodestyle.StyleGuide(quiet=True)
        result = pep8style.check_files(['models/amenity.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")


class TestInheritBaseModel(unittest.TestCase):
    """Test if Amenity inherits from BaseModel"""
    def test_instance(self):
        """Check if Amenity is an instance of BaseModel"""
        amenity = Amenity()
        self.assertIsInstance(amenity, Amenity)
        self.assertTrue(issubclass(type(amenity), BaseModel))
        self.assertEqual(str(type(amenity)), "<class 'models.amenity.Amenity'>")


class TestAmenityBaseModel(unittest.TestCase):
    """Test Amenity class"""
    def test_instances(self):
        with patch('models.amenity'):
            instance = Amenity()
            self.assertEqual(type(instance), Amenity)
            instance.name = "Barbie"
            expected_attrs_types = {
                "id": str,
                "created_at": datetime,
                "updated_at": datetime,
                "name": str,
            }
            inst_dict = instance.to_dict()
            expected_dict_attrs = [
                "id",
                "created_at",
                "updated_at",
                "name",
                "__class__"
            ]
            self.assertCountEqual(inst_dict.keys(), expected_dict_attrs)
            self.assertEqual(inst_dict['name'], 'Barbie')
            self.assertEqual(inst_dict['__class__'], 'Amenity')

            for attr, types in expected_attrs_types.items():
                with self.subTest(attr=attr, typ=types):
                    self.assertIn(attr, instance.__dict__)
                    self.assertIs(type(instance.__dict__[attr]), types)
            self.assertEqual(instance.name, "Barbie")

    def test_user_id_and_create_at(self):
        """Testing id for every user"""
        amenity_1 = Amenity()
        sleep(2)
        amenity_2 = Amenity()
        sleep(2)
        amenity_3 = Amenity()
        sleep(2)
        list_amenities = [amenity_1, amenity_2, amenity_3]
        for instance in list_amenities:
            amenity_id = instance.id
            with self.subTest(amenity_id=amenity_id):
                self.assertIs(type(amenity_id), str)
        self.assertNotEqual(amenity_1.id, amenity_2.id)
        self.assertNotEqual(amenity_1.id, amenity_3.id)
        self.assertNotEqual(amenity_2.id, amenity_3.id)
        self.assertTrue(amenity_1.created_at <= amenity_2.created_at)
        self.assertTrue(amenity_2.created_at <= amenity_3.created_at)
        self.assertNotEqual(amenity_1.created_at, amenity_2.created_at)
        self.assertNotEqual(amenity_1.created_at, amenity_3.created_at)
        self.assertNotEqual(amenity_3.created_at, amenity_2.created_at)

    def test_str_method(self):
        """
        Testing str magic method
        """
        inst = Amenity()
        str_output = "[Amenity] ({}) {}".format(inst.id, inst.__dict__)
        self.assertEqual(str_output, str(inst))

    @patch('models.storage')
    def test_save_method(self, mock_storage):
        """Testing save method and if it updates"""
        instance5 = Amenity()
        created_at = instance5.created_at
        sleep(2)
        updated_at = instance5.updated_at
        instance5.save()
        new_created_at = instance5.created_at
        sleep(2)
        new_updated_at = instance5.updated_at
        self.assertNotEqual(updated_at, new_updated_at)
        self.assertEqual(created_at, new_created_at)
        self.assertTrue(mock_storage.save.called)


class TestAmenity(unittest.TestCase):
    """Test the Amenity class"""

    def test_is_subclass(self):
        """Test that Amenity is a subclass of BaseModel"""
        amenity = Amenity()
        self.assertIsInstance(amenity, BaseModel)
        self.assertTrue(hasattr(amenity, "id"))
        self.assertTrue(hasattr(amenity, "created_at"))
        self.assertTrue(hasattr(amenity, "updated_at"))

    def test_name_attr(self):
        """Test that Amenity has attribute name, and it's an empty string"""
        amenity = Amenity()
        self.assertTrue(hasattr(amenity, "name"))
        self.assertEqual(amenity.name, "")

    def test_to_dict_creates_dict(self):
        """Test to_dict method creates a dictionary with proper attrs"""
        am = Amenity()
        new_d = am.to_dict()
        self.assertEqual(type(new_d), dict)
        self.assertFalse("_sa_instance_state" in new_d)
        for attr in am.__dict__:
            if attr != "_sa_instance_state":
                self.assertTrue(attr in new_d)
        self.assertTrue("__class__" in new_d)

    def test_to_dict_values(self):
        """Test that values in dict returned from to_dict are correct"""
        t_format = "%Y-%m-%dT%H:%M:%S.%f"
        am = Amenity()
        new_d = am.to_dict()
        self.assertEqual(new_d["__class__"], "Amenity")
        self.assertEqual(type(new_d["created_at"]), str)
        self.assertEqual(type(new_d["updated_at"]), str)
        self.assertEqual(new_d["created_at"], am.created_at.strftime(t_format))
        self.assertEqual(new_d["updated_at"], am.updated_at.strftime(t_format))

    def test_str(self):
        """Test that the str method has the correct output"""
        amenity = Amenity()
        string = "[Amenity] ({}) {}".format(amenity.id, amenity.__dict__)
        self.assertEqual(string, str(amenity))