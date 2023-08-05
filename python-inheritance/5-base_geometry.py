"""
Module: my_geometry

This module defines the BaseGeometry class.
"""

class BaseGeometry:
    """
    BaseGeometry class serves as a base for geometry classes.

    Public Methods:
        area(self): Calculate the area of the geometry.

        integer_validator(self, name, value): Validate the integer value.

    Public Attributes:
        None

    Raises:
        Exception: Always raises an Exception with the message "area() is not implemented".
        TypeError: Raised by the integer_validator if value is not an integer.
        ValueError: Raised by the integer_validator if value is less than or equal to 0.
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

    def integer_validator(self, name, value):
        """
        Validate the integer value.

        Args:
            name (str): The name of the value.
            value: The value to be validated.

        Raises:
            TypeError: Raised if value is not an integer.
            ValueError: Raised if value is less than or equal to 0.
        """
        if not isinstance(value, int):
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")