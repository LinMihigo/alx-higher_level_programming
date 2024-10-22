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
from io import StringIO
import sys


class TestRectangle(unittest.TestCase):
    """Test cases for the Rectangle class."""

    def test_rectangle_init(self):
        r = Rectangle(10, 5)
        self.assertEqual(r.width, 10)
        self.assertEqual(r.height, 5)

    def test_str_width(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle("1", 2)

    def test_str_height(self):
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(1, "2")

    def test_str_x(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(1, 2, "3")

    def test_str_y(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(1, 2, 3, "4")

    def test_neg_width(self):
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            Rectangle(-1, 2)

    def test_neg_height(self):
        with self.assertRaisesRegex(ValueError, "height must be > 0"):
            Rectangle(1, -2)

    def test_zero_width(self):
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            Rectangle(0, 2)

    def test_zero_height(self):
        with self.assertRaisesRegex(ValueError, "height must be > 0"):
            Rectangle(1, 0)

    def test_neg_x(self):
        with self.assertRaisesRegex(ValueError, "x must be >= 0"):
            Rectangle(1, 2, -3)

    def test_neg_y(self):
        with self.assertRaisesRegex(ValueError, "y must be >= 0"):
            Rectangle(1, 2, 3, -4)

    def test_rectangle_area(self):
        r = Rectangle(10, 5)
        self.assertEqual(r.area(), 50)

    # display() method tests
    def setUp(self):
        self.output = StringIO()
        sys.stdout = self.output

    def tearDown(self):
        sys.stdout = sys.__stdout__

    def test_display_basic(self):
        r = Rectangle(4, 3)
        r.display()
        self.assertEqual(self.output.getvalue(), "####\n####\n####\n")

    def test_display_with_x(self):
        r = Rectangle(4, 2, 2)
        r.display()
        self.assertEqual(self.output.getvalue(), "  ####\n  ####\n")

    def test_display_with_y(self):
        r = Rectangle(3, 2, 0, 2)
        r.display()
        self.assertEqual(self.output.getvalue(), "\n\n###\n###\n")

    def test_display_with_x_y(self):
        r = Rectangle(2, 3, 3, 1)
        r.display()
        self.assertEqual(self.output.getvalue(), "\n   ##\n   ##\n   ##\n")

    # __str__() method
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

    def test_rectangle_save_class_call_to_file(self):
        Rectangle.save_to_file([Rectangle(1, 2)])
        with open("Rectangle.json", "r") as file:
            content = file.read()
            output = '[{"x": 0, "y": 0, "id": 17, "height": 2, "width": 1}]'
            self.assertEqual(content, output)

    def test_rectangle_save_None_to_file(self):
        Rectangle.save_to_file(None)
        with open("Rectangle.json", "r") as file:
            content = file.read()
            self.assertEqual(content, "[]")

    def test_rectangle_save_empty_to_file(self):
        Rectangle.save_to_file([])
        with open("Rectangle.json", "r") as file:
            content = file.read()
            self.assertEqual(content, "[]")

    def test_rectangle_load_from_file(self):
        r1 = Rectangle(10, 7, 2, 8)
        r2 = Rectangle(2, 4)
        Rectangle.save_to_file([r1, r2])
        instances = Rectangle.load_from_file()
        self.assertEqual(len(instances), 2)
        self.assertTrue(isinstance(instances[0], Rectangle))

    # Test to dictionary
    def test_to_dictionary_basic(self):
        r = Rectangle(10, 2, 1, 9, 1)
        expected_dict = {'id': 1, 'width': 10, 'height': 2, 'x': 1, 'y': 9}
        self.assertEqual(r.to_dictionary(), expected_dict)

    def test_to_dictionary_no_id(self):
        r = Rectangle(4, 6, 2, 2)
        expected_dict = {'id': r.id, 'width': 4, 'height': 6, 'x': 2, 'y': 2}
        self.assertEqual(r.to_dictionary(), expected_dict)

    def test_to_dictionary_with_update(self):
        r = Rectangle(5, 7, 3, 1, 89)
        r.update(10, 3, 4, 2, 1)
        expected_dict = {'id': 10, 'width': 3, 'height': 4, 'x': 2, 'y': 1}
        self.assertEqual(r.to_dictionary(), expected_dict)

    def test_to_dictionary_type(self):
        r = Rectangle(1, 2)
        self.assertIsInstance(r.to_dictionary(), dict)


if __name__ == "__main__":
    unittest.main()
