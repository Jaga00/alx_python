'''
This module defines a class Rectangle that represents a Rectangle.

class Rectangle:
A class representing a rectangle.

'''
from models.base import Base

class Rectangle(Base):
    """
    A class representing a rectangle.
    """

    def __init__(self, width, height, x=0, y=0, id=None):
        """
        Initialize a new instance of the Rectangle class.

        Args:
            width (int): The width of the rectangle.
            height (int): The height of the rectangle.
            x (int): The x-coordinate of the rectangle's position.
            y (int): The y-coordinate of the rectangle's position.
            id (int): An optional ID for the rectangle.
        """
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """Get the width of the rectangle."""
        return self.__width

    @width.setter
    def width(self, value):
        """Set the width of the rectangle."""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """Get the height of the rectangle."""
        return self.__height

    @height.setter
    def height(self, value):
        """Set the height of the rectangle."""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """Get the x-coordinate of the rectangle's position."""
        return self.__x

    @x.setter
    def x(self, value):
        """Set the x-coordinate of the rectangle's position."""
        if not isinstance(value, int):
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """Get the y-coordinate of the rectangle's position."""
        return self.__y

    @y.setter
    def y(self, value):
        """Set the y-coordinate of the rectangle's position."""
        if not isinstance(value, int):
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """Calculate and return the area value of the Rectangle instance."""
        return self.__width * self.__height    
    
    def display(self):
        """Display the Rectangle instance using the character '#'."""
        for i in range(self.__y):
            print()
        for i in range(self.__height):
            print(" " * self.__x + '#' * self.__width)

    def __str__(self):
        """Return a string representation of the Rectangle instance."""
        return f"[Rectangle] ({self.id}) {self.x}/{self.y} - {self.width}/{self.height}"        
    
    def update(self, *args, **kwargs):
        """
        Update the attributes of the Rectangle instance.

        Args:
            *args: The attributes in the order: id, width, height, x, y.
            **kwargs: Key-worded arguments for updating attributes.
        """
        if args:
            num_args = len(args)
            if num_args > 0:
                self.id = args[0]
            if num_args > 1:
                self.width = args[1]
            if num_args > 2:
                self.height = args[2]
            if num_args > 3:
                self.x = args[3]
            if num_args > 4:
                self.y = args[4]    

        elif kwargs:
            for key, value in kwargs.items():
                if key == 'id':
                    self.id = value
                elif key == 'width':
                    self.width = value
                elif key == 'height':
                    self.height = value
                elif key == 'x':
                    self.x = value
                elif key == 'y':
                    self.y = value



