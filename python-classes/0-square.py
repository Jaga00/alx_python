"""
This module defines a class Square that represents a square.

Class Square:
    A class representing a square with a given size.

Attributes:
    size (int): The size of the square.

Methods:
    __init__(self, size=0): Initialize the Square object with an optional size.
    
"""

class Square:
    """
        A class representing a square with a given size.

        Attributes:
            size (int): The size of the square.

        Methods:
            __init__(self, size): Initialize the Square object with no type/value verification.
        """
    
    def __init__(self, size):
        """
        Initialize the Square object with a size.

        Args:
            size: The size of the square (no type/value verification).
        """
        self.__size = size  # Private instance attribute, denoted by double underscores
