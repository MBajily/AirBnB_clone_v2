#!/usr/bin/python3
"""
Test module for the Review class
"""
from tests.test_models.test_base_model import TestBaseModel
from models.review import Review


class TestReview(TestBaseModel):
    """
    Test class for the Review class
    """

    def __init__(self, *args, **kwargs):
        """
        Initialization method
        """
        super().__init__(*args, **kwargs)
        self.name = "Review"
        self.value = Review

    def test_user_id(self):
        """
        Test user_id attribute of Review
        """
        new = self.value()
        self.assertEqual(type(new.user_id), str)

    def test_text(self):
        """
        Test text attribute of Review
        """
        new = self.value()
        self.assertEqual(type(new.text), str)

    def test_place_id(self):
        """
        Test place_id attribute of Review
        """
        new = self.value()
        self.assertEqual(type(new.place_id), str)
