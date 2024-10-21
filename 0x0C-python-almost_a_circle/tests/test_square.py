#!/usr/bin/python3
"""
Unit tests for the Square class.

Test methods:
    test_square_init:
        Ensures the Square is initialized with the correct attributes.

    test_square_area:
        Verifies the area calculation is correct.

    test_square_str:
        Verifies the string representation of the square.

    test_square_update:
        Ensures the update method works with both positional and keyword
        arguments.

    test_square_save_to_file:
        Ensures that the Square is correctly saved to a JSON file.

    test_square_load_from_file:
        Ensures that the Square is correctly loaded from a JSON file.
"""
import unittest
from models.square import Square


class TestSquare(unittest.TestCase):
    """Test cases for the Square class."""

    def test_square_init(self):
        s = Square(5)
        self.assertEqual(s.size, 5)
        self.assertEqual(s.width, 5)
        self.assertEqual(s.height, 5)

    def test_square_area(self):
        s = Square(4)
        self.assertEqual(s.area(), 16)

    def test_square_str(self):
        s = Square(5, 2, 3, 12)
        self.assertEqual(str(s), "[Square] (12) 2/3 - 5")

    def test_square_update(self):
        s = Square(5)
        s.update(89, 2, 3, 4)
        self.assertEqual(s.id, 89)
        self.assertEqual(s.size, 2)
        self.assertEqual(s.x, 3)
        self.assertEqual(s.y, 4)

    def test_square_save_to_file(self):
        s1 = Square(5)
        s2 = Square(7)
        Square.save_to_file([s1, s2])
        with open("Square.json", "r") as file:
            content = file.read()
            self.assertTrue('"size": 5' in content)
            self.assertTrue('"size": 7' in content)

    def test_square_load_from_file(self):
        s1 = Square(5)
        s2 = Square(7)
        Square.save_to_file([s1, s2])
        instances = Square.load_from_file()
        self.assertEqual(len(instances), 2)
        self.assertTrue(isinstance(instances[0], Square))
