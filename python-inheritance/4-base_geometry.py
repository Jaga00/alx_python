"""
Module: my_geometry

This module defines the BaseGeometry class.
"""

class BaseGeometry:
    """
    BaseGeometry class serves as a base for geometry classes.

    Public Methods:
        area(self): Calculate the area of the geometry.

    Public Attributes:
        None

    Raises:
        Exception: Always raises an Exception with the message "area() is not implemented".
    """

    def area(self):
        """
        Calculate the area of the geometry.

        Raises:
            Exception: Always raises an Exception with the message "area() is not implemented".
        """
        raise Exception("area() is not implemented")