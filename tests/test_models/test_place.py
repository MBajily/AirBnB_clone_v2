#!/usr/bin/python3
"""
Test module for the Place class
"""
from models.place import Place


class TestPlace(TestBaseModel):
    """
    Test class for the Place class
    """

    def __init__(self, *args, **kwargs):
        """
        Initialization method
        """
        super().__init__(*args, **kwargs)
        self.name = "Place"
        self.value = Place

    def test_city_id(self):
        """
        Test city_id attribute of Place
        """
        new = self.value()
        self.assertEqual(type(new.city_id), str)

    def test_user_id(self):
        """
        Test user_id attribute of Place
        """
        new = self.value()
        self.assertEqual(type(new.user_id), str)

    def test_name(self):
        """
        Test name attribute of Place
        """
        new = self.value()
        self.assertEqual(type(new.name), str)

    def test_description(self):
        """
        Test description attribute of Place
        """
        new = self.value()
        self.assertEqual(type(new.description), str)

    def test_number_rooms(self):
        """
        Test number_rooms attribute of Place
        """
        new = self.value()
        self.assertEqual(type(new.number_rooms), int)

    def test_latitude(self):
        """
        Test latitude attribute of Place
        """
        new = self.value()
        self.assertEqual(type(new.latitude), float)

    def test_longitude(self):
        """
        Test longitude attribute of Place
        """
        new = self.value()
        self.assertEqual(type(new.longitude), float)

    def test_amenity_ids(self):
        """
        Test amenity_ids attribute of Place
        """
        new = self.value()
        self.assertEqual(type(new.amenity_ids), list)

    def test_number_bathrooms(self):
        """
        Test number_bathrooms attribute of Place
        """
        new = self.value()
        self.assertEqual(type(new.number_bathrooms), int)

    def test_max_guest(self):
        """
        Test max_guest attribute of Place
        """
        new = self.value()
        self.assertEqual(type(new.max_guest), int)

    def test_price_by_night(self):
        """
        Test price_by_night attribute of Place
        """
        new = self.value()
        self.assertEqual(type(new.price_by_night), int)
