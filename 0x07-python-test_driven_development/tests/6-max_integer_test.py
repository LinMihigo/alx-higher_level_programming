#!/usr/bin/python3
"""Unittests for max_integer"""


import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):
    """Define unittests for max_integer function"""

    def test_max_at_end(self):
        """Test list where max value is at the end"""
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)

    def test_max_at_beginning(self):
        """Test list where max value is at the beginning"""
        self.assertEqual(max_integer([4, 3, 2, 1]), 4)

    def test_max_in_middle(self):
        """Test list where max value is in the middle"""
        self.assertEqual(max_integer([1, 4, 3, 2]), 4)

    def test_single_element(self):
        """Test list with a single element"""
        self.assertEqual(max_integer([5]), 5)

    def test_empty_list(self):
        """Test empty list"""
        self.assertEqual(max_integer([]), None)

    def test_negative_numbers(self):
        """Test list with all negative numbers"""
        self.assertEqual(max_integer([-1, -2, -3, -4]), -1)

    def test_mixed_numbers(self):
        """Test list with a mix of positive and negative numbers"""
        self.assertEqual(max_integer([1, -2, 3, -4]), 3)

    def test_identical_elements(self):
        """Test list where all elements are identical"""
        self.assertEqual(max_integer([5, 5, 5, 5]), 5)

    def test_float_numbers(self):
        """Test list with float numbers"""
        self.assertEqual(max_integer([1.5, 2.5, 3.5]), 3.5)

    def test_string_list(self):
        """Test list with string elements"""
        self.assertEqual(max_integer(['a', 'b', 'c']), 'c')

    def test_mixed_type(self):
        """Test list with mixed types should raise TypeError"""
        with self.assertRaises(TypeError):
            max_integer([1, 'a', 3])

if __name__ == "__main__":
    unittest.main()
