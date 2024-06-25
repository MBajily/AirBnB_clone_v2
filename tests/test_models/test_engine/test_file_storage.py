#!/usr/bin/python3
"""Module for testing the FileStorage class"""
import unittest
from models import storage
from models.base_model import BaseModel
import os


class test_fileStorage(unittest.TestCase):
    """Class to test the FileStorage methods"""

    def setUp(self):
        """Set up the test environment"""
        delete_list = []
        for key in storage._FileStorage__objects.keys():
            delete_list.append(key)
        for key in delete_list:
            del storage._FileStorage__objects[key]

    def tearDown(self):
        """Remove the storage file at the end of the tests"""
        try:
            os.remove('file.json')
        except:
            pass

    def test_new_object_added(self):
        """Test if a new object is correctly added to __objects"""
        new = BaseModel()
        for obj in storage.all().values():
            tmp = obj
        self.assertTrue(tmp is obj)
    
    def test_objects_empty(self):
        """Test if __objects is initially empty"""
        self.assertEqual(len(storage.all()), 0)

    def test_base_model_save(self):
        """Test if the BaseModel save method doesn't create a file"""
        new = BaseModel()
        self.assertFalse(os.path.exists('file.json'))

    def test_all_returns_dict(self):
        """Test if all method properly returns a dictionary"""
        new = BaseModel()
        tmp = storage.all()
        self.assertIsInstance(tmp, dict)

    def test_data_saved_to_file(self):
        """Test if data is saved to the file"""
        new = BaseModel()
        thing = new.to_dict()
        new.save()
        new2 = BaseModel(**thing)
        self.assertNotEqual(os.path.getsize('file.json'), 0)

    def test_save_method(self):
        """Test the save method of FileStorage"""
        new = BaseModel()
        storage.save()
        self.assertTrue(os.path.exists('file.json'))

    def test_reload_empty_file(self):
        """Test loading from an empty file"""
        with open('file.json', 'w') as f:
            pass
        with self.assertRaises(ValueError):
            storage.reload()

    def test_reload_nonexistent_file(self):
        """Test if nothing happens when the file does not exist"""
        self.assertEqual(storage.reload(), None)

    def test_reload_method(self):
        """Test the reload method successfully loads the file to __objects"""
        new = BaseModel()
        storage.save()
        storage.reload()
        for obj in storage.all().values():
            loaded = obj
        self.assertEqual(new.to_dict()['id'], loaded.to_dict()['id'])

    def test_base_model_save_calls_storage(self):
        """Test if the BaseModel save method calls the storage save method"""
        new = BaseModel()
        new.save()
        self.assertTrue(os.path.exists('file.json'))

    def test_key_format(self):
        """Test if the key is properly formatted"""
        new = BaseModel()
        _id = new.to_dict()['id']
        for key in storage.all().keys():
            tmp = key
        self.assertEqual(tmp, 'BaseModel' + '.' + _id)

    def test_file_path_type(self):
        """Test if __file_path is of type string"""
        self.assertEqual(type(storage._FileStorage__file_path), str)

    def test_objects_type(self):
        """Test if __objects is of type dict"""
        self.assertEqual(type(storage.all()), dict)

    def test_storage_object_created(self):
        """Test the storage object is created as an instance of FileStorage"""
        from models.engine.file_storage import FileStorage
        print(type(storage))
        self.assertEqual(type(storage), FileStorage)
