'''
This module defines a class Square that represents a Square.

class Square:
A class representing a square.

'''

from models.rectangle import Rectangle

class Square(Rectangle):
    """
    A class representing a square.
    """

    def __init__(self, size, x=0, y=0, id=None):
        """
        Initialize a new instance of the Square class.

        Args:
            size (int): The size of the square (width and height).
            x (int): The x-coordinate of the square's position.
            y (int): The y-coordinate of the square's position.
            id (int): An optional ID for the square.
        """
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """Get the size of the square."""
        return self.width

    @size.setter
    def size(self, value):
        """Set the size of the square (width and height)."""
        self.width = value
        self.height = value

    def __str__(self):
        """Return a string representation of the Square instance."""
        return f"[Square] ({self.id}) {self.x}/{self.y} - {self.width}"