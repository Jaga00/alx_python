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
        if isinstance(value, int):
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")


class Rectangle(BaseGeometry):
    """
    Rectangle class inherits from BaseGeometry.

    Public Methods:
        None (Inherits area() and integer_validator() from BaseGeometry).

    Public Attributes:
        None (width and height are private).

    Raises:
        None
    """

    def __init__(self, width, height):
        """
        Initialize a new Rectangle instance with width and height.

        Args:
            width (int): The width of the rectangle.
            height (int): The height of the rectangle.

        Raises:
            TypeError: Raised by integer_validator if width or height is not an integer.
            ValueError: Raised by integer_validator if width or height is less than or equal to 0.
        """
        self.__width = width
        self.__height = height
        self.integer_validator("width", width)
        self.integer_validator("height", height)