#!/usr/bin/python3
"""Define LockedClass"""


class LockedClass:
    """Class that only allows dynamic creation of the 'first_name'
        instance attribute.

    The LockedClass uses the `__slots__` mechanism to prevent users from
    creating any new attributes, except for 'first_name'.

    Attributes:
        first_name (str): The only attribute that can be dynamically
        created.
    """
    __slots__ = ['first_name']
