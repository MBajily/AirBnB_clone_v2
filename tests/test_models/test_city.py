#!/usr/bin/python3
"""
Test module for the City class
"""
from tests.test_models.test_base_model import TestBaseModel
from models.city import City
import pycodestyle


class TestCity(TestBaseModel):
    """
    Test class for the City class
    """

    def __init__(self, *args, **kwargs):
        """
        Initialization method
        """
        super().__init__(*args, **kwargs)
        self.name = "City"
        self.value = City

    def test_state_id(self):
        """
        Test state_id attribute of City
        """
        new = self.value()
        self.assertEqual(type(new.state_id), str)

    def test_name(self):
        """
        Test name attribute of City
        """
        new = self.value()
        self.assertEqual(type(new.name), str)


class TestPEP8(unittest.TestCase):
    """
    Test class for PEP 8 style
    """

    def test_pep8_city(self):
        """
        Test PEP 8 style for City module
        """
        pep8style = pycodestyle.StyleGuide(quiet=True)
        result = pep8style.check_files(['models/city.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")


class TestCity(unittest.TestCase):
    """
    Test class for the City class
    """

    @classmethod
    def setUpClass(cls):
        """
        Set up class method
        """
        cls.city = City()
        cls.city.name = "LA"
        cls.city.state_id = "CA"

    @classmethod
    def tearDownClass(cls):
        """
        Tear down class method
        """
        del cls.city

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
        Test PEP 8 style for City class
        """
        style = pep8.StyleGuide(quiet=True)
        p = style.check_files(['models/city.py'])
        self.assertEqual(p.total_errors, 0, "Fix PEP 8 style")

    def test_checking_for_docstring(self):
        """
        Test checking for docstrings in City class
        """
        self.assertIsNotNone(City.__doc__)

    def test_attributes(self):
        """
        Test if City class has required attributes
        """
        self.assertTrue('id' in self.city.__dict__)
        self.assertTrue('created_at' in self.city.__dict__)
        self.assertTrue('updated_at' in self.city.__dict__)
        self.assertTrue('state_id' in self.city.__dict__)
        self.assertTrue('name' in self.city.__dict__)

    def test_is_subclass(self):
        """
        Test if City is a subclass of BaseModel
        """
        self.assertTrue(issubclass(self.city.__class__, BaseModel), True)

    def test_attribute_types(self):
        """
        Test attribute types for City class
        """
        self.assertEqual(type(self.city.name), str)
        self.assertEqual(type(self.city.state_id), str)

    def test_save(self):
        """
        Test if save method works for City class
        """
        self.city.save()
        self.assertNotEqual(self.city.created_at, self.city.updated_at)

    def test_to_dict(self):
        """
        Test if to_dict method works for City class
        """
        self.assertEqual('to_dict' in dir(self.city), True)


if __name__ == "__main__":
    unittest.main()
