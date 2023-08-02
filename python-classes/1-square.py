class Square:
    def __init__(self, size=0):
        """
        Initialize the Square object with an optional size.

        Args:
            size (int, optional): The size of the square (default is 0).
                It must be an integer, otherwise raise a TypeError exception.
                If size is less than 0, raise a ValueError exception.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")

        if size < 0:
            raise ValueError("size must be >= 0")

        self.__size = size  # Private instance attribute, denoted by double underscores

   