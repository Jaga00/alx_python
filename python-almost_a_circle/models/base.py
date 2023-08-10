'''
This module defines a class Base that represents a Base.

class Base:
The base class for managing id attribute in all future classes.

'''

class Base:
    """
    The base class for managing id attribute in all future classes.
    """

    __nb_objects = 0

    def __init__(self, id=None):
        """
        Initialize a new instance of the Base class.

        Args:
            id (int): An integer value to assign to the id attribute.
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects