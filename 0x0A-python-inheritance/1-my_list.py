#!/usr/bin/python3
"""Define MyList class"""


class MyList(list):
    """
    A custom list class that inherits from the built-in list class.

    Methods:
    --------
    print_sorted():
        Prints the list sorted in ascending order.
    """

    def print_sorted(self):
        """
        Prints the elements of the list in ascending order.

        This method does not modify the original list, but prints a
        sorted version.
        """
        sorted_list = sorted(self)
        print(sorted_list)
