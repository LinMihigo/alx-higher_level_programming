#!/usr/bin/python3
"""
Unit tests for the Base class.

Test methods:
    test_base_id_auto_increment:
        Ensures the ID is automatically incremented when not specified.

    test_base_id_specified:
        Ensures the ID is set correctly when specified.

    test_to_json_string:
        Verifies that the method correctly converts a list of dictionaries
        to a JSON string.

    test_from_json_string:
        Verifies that the method correctly converts a JSON string to a list
        of dictionaries.

    test_save_to_file:
        Ensures that an empty list is saved as "[]" to the file.

    test_load_from_file_empty:
        Ensures that loading from a nonexistent file returns an empty list.
"""
import unittest
from models.base import Base


class TestBase(unittest.TestCase):
    """Test cases for the Base class."""

    def test_base_id_auto_increment(self):
        b1 = Base()
        b2 = Base()
        self.assertEqual(b1.id + 1, b2.id)

    def test_base_id_specified(self):
        b = Base(100)
        self.assertEqual(b.id, 100)

    def test_to_json_string(self):
        dict_list = [{'id': 12}, {'id': 7}]
        json_str = Base.to_json_string(dict_list)
        self.assertEqual(type(json_str), str)
        self.assertTrue('"id": 12' in json_str)

    def test_from_json_string(self):
        json_str = '[{"id": 12}, {"id": 7}]'
        dict_list = Base.from_json_string(json_str)
        self.assertEqual(len(dict_list), 2)
        self.assertEqual(dict_list[0]['id'], 12)

    def test_save_to_file(self):
        Base.save_to_file(None)
        with open("Base.json", "r") as file:
            content = file.read()
            self.assertEqual(content, "[]")

    def test_load_from_file_empty(self):
        instances = Base.load_from_file()
        self.assertEqual(instances, [])


if __name__ == "__main__":
    unittest.main()
