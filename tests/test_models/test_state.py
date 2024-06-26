#!/usr/bin/python3
"""
Test module for the State class
"""
from tests.test_models.test_base_model import TestBaseModel
from models.state import State


class TestState(TestBaseModel):
    """
    Test class for the State class
    """

    def __init__(self, *args, **kwargs):
        """
        Initialization method
        """
        super().__init__(*args, **kwargs)
        self.name = "State"
        self.value = State

    def test_name(self):
        """
        Test name attribute of State
        """
        new = self.value()
        self.assertEqual(type(new.name), str)
