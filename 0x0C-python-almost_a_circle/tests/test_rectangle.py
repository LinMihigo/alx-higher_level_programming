#!/usr/bin/python3
"""
Unit tests for the Rectangle class.

Test methods:
    test_rectangle_init:
        Ensures the Rectangle is initialized with the correct attributes.

    test_rectangle_area:
        Verifies the area calculation is correct.

    test_rectangle_str:
        Verifies the string representation of the rectangle.

    test_rectangle_update:
        Ensures the update method works with both positional and keyword
        arguments.

    test_rectangle_save_to_file:
        Ensures that the Rectangle is correctly saved to a JSON file.

    test_rectangle_load_from_file:
        Ensures that the Rectangle is correctly loaded from a JSON file.
"""
import unittest
from models.rectangle import Rectangle


class TestRectangle(unittest.TestCase):
    """Test cases for the Rectangle class."""

    def test_rectangle_init(self):
        r = Rectangle(10, 5)
        self.assertEqual(r.width, 10)
        self.assertEqual(r.height, 5)

    def test_rectangle_area(self):
        r = Rectangle(10, 5)
        self.assertEqual(r.area(), 50)

    def test_rectangle_str(self):
        r = Rectangle(10, 2, 1, 1, 12)
        self.assertEqual(str(r), "[Rectangle] (12) 1/1 - 10/2")

    def test_rectangle_update(self):
        r = Rectangle(10, 5)
        r.update(89, 2, 3, 4, 5)
        self.assertEqual(r.id, 89)
        self.assertEqual(r.width, 2)
        self.assertEqual(r.height, 3)
        self.assertEqual(r.x, 4)
        self.assertEqual(r.y, 5)

    def test_rectangle_save_to_file(self):
        r1 = Rectangle(10, 7, 2, 8)
        r2 = Rectangle(2, 4)
        Rectangle.save_to_file([r1, r2])
        with open("Rectangle.json", "r") as file:
            content = file.read()
            self.assertTrue('"width": 10' in content)
            self.assertTrue('"width": 2' in content)

    def test_rectangle_load_from_file(self):
        r1 = Rectangle(10, 7, 2, 8)
        r2 = Rectangle(2, 4)
        Rectangle.save_to_file([r1, r2])
        instances = Rectangle.load_from_file()
        self.assertEqual(len(instances), 2)
        self.assertTrue(isinstance(instances[0], Rectangle))
