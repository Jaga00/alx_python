"""
This module defines a class Square that represents a square.

Class Square:
    A class representing a square with a given size.

Attributes:
    size (int): The size of the square.

Methods:
    __init__(self, size=0): Initialize the Square object with an optional size.
    area(self): Calculate the area of the square.
    my_print(self): Print the square using the character '#'.
"""

class Square:
 
    """
        A class representing a square with a given size.

        Attributes:
            size (int): The size of the square.

        Methods:
            __init__(self, size=0): Initialize the Square object with an optional size.
            area(self): Calculate the area of the square.
            my_print(self): Print the square using the character '#'.
        """    
     
    def __init__(self, size=0):
        """
        Initialize the Square object with an optional size.

        Args:
            size (int, optional): The size of the square (default is 0).
        """
        self.size = size  # Uses the property setter to set the size

    @property
    def size(self):
        """
        Get the size of the square.

        Returns:
            int: The size of the square.
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        Set the size of the square.

        Args:
            value: The new size of the square.
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")

        if value < 0:
            raise ValueError("size must be >= 0")

        self.__size = value  # Private instance attribute, denoted by double underscores

    def area(self):
        """
        Calculate the area of the square.

        Returns:
            int: The area of the square.
        """
        return self.__size * self.__size

    def my_print(self):
        """Print the square with the character #."""
        if self.__size == 0:
            print()
        else:
            for _ in range(self.__size):
                print("#" * self.__size)