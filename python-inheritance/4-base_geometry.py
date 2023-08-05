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

    def __dir__(cls) -> None:
        # get list of all attributes for this class and exclude __init_subclass__
        attributes = super().__dir__()

        list_to_return = []

        for attr in attributes:
            if attr != "__init_subclass__":
                # append this to the list_to_return
                list_to_return.append(attr)

        return list_to_return

    def area(self):
        """
        Calculate the area of the geometry.

        Raises:
            Exception: Always raises an Exception with the message "area() is not implemented".
        """
        raise Exception("area() is not implemented")
    