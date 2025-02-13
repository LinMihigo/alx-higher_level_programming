#!/usr/bin/python3
"""
Unit tests for the Square class.

Test methods:
    test_square_init:
        Ensures the Square is initialized with the correct attributes.
if __name__ == "__main__":
    unittest.main()
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
import os
from models.square import Square


class TestSquare(unittest.TestCase):
    """Test cases for the Square class."""

    def test_square_init(self):
        s = Square(5)
        self.assertEqual(s.size, 5)
        self.assertEqual(s.width, 5)
        self.assertEqual(s.height, 5)

    def test_square_with_x(self):
        s = Square(1, 2)
        self.assertEqual(s.size, 1)
        self.assertEqual(s.width, 1)
        self.assertEqual(s.height, 1)
        self.assertEqual(s.x, 2)

    def test_square_with_y(self):
        s = Square(1, 2, 3)
        self.assertEqual(s.size, 1)
        self.assertEqual(s.width, 1)
        self.assertEqual(s.height, 1)
        self.assertEqual(s.x, 2)
        self.assertEqual(s.y, 3)

    def test_square_neg_size(self):
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            Square(-1)

    def test_square_zero_size(self):
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            Square(0)

    def test_square_neg_x(self):
        with self.assertRaisesRegex(ValueError, "x must be >= 0"):
            Square(1, -2)

    def test_square_neg_y(self):
        with self.assertRaisesRegex(ValueError, "y must be >= 0"):
            Square(1, 2, -3)

    def test_square_str_size(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square("1")

    def test_square_str_x(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Square(1, "2")

    def test_square_str_y(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Square(1, 2, "3")

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

    def test_to_dictionary_basic(self):
        s = Square(5, 2, 1, 10)
        expected_dict = {'id': 10, 'size': 5, 'x': 2, 'y': 1}
        self.assertEqual(s.to_dictionary(), expected_dict)

    def test_to_dictionary_no_id(self):
        s = Square(3, 1, 0)
        expected_dict = {'id': s.id, 'size': 3, 'x': 1, 'y': 0}
        self.assertEqual(s.to_dictionary(), expected_dict)

    def test_to_dictionary_with_update(self):
        s = Square(7, 4, 3, 50)
        s.update(1, 6, 2, 0)
        expected_dict = {'id': 1, 'size': 6, 'x': 2, 'y': 0}
        self.assertEqual(s.to_dictionary(), expected_dict)

    def test_to_dictionary_type(self):
        s = Square(9)
        self.assertIsInstance(s.to_dictionary(), dict)

    def tearDown(self):
        """Remove the file after each test."""
        try:
            os.remove("Square.json")
        except FileNotFoundError:
            pass

    def test_save_to_file_single_square(self):
        s = Square(5, 1, 2, 10)
        Square.save_to_file([s])
        with open("Square.json", "r") as file:
            content = file.read()
        expected = '[{"id": 10, "x": 1, "size": 5, "y": 2}]'
        self.assertEqual(content, expected)

    def test_save_to_file_multiple_squares(self):
        s1 = Square(3, 1, 2, 10)
        s2 = Square(4, 0, 0, 20)
        Square.save_to_file([s1, s2])
        with open("Square.json", "r") as file:
            content = file.read()
        expected = ('[{"id": 10, "x": 1, "size": 3, "y": 2}, '
                    '{"id": 20, "x": 0, "size": 4, "y": 0}]')
        self.assertEqual(content, expected)

    def test_save_to_file_empty_list(self):
        Square.save_to_file([])
        with open("Square.json", "r") as file:
            content = file.read()
        self.assertEqual(content, '[]')

    def test_save_to_file_none(self):
        Square.save_to_file(None)
        with open("Square.json", "r") as file:
            content = file.read()
        self.assertEqual(content, '[]')


if __name__ == "__main__":
    unittest.main()
