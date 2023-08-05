'''
a function that returns True if the
object is an instance of a class that inherited
(directly or indirectly) from the specified class ; otherwise False.
'''

def inherits_from(obj, a_class):
    

    """
    Check if the object is an instance of a class
    that inherited (directly or indirectly) from the specified class.

    Args:
        obj: The object to check.
        a_class: The class to compare with.

    Returns:
        bool: True if the object is an instance of a class
        that inherited from the specified class; otherwise False.
    """

    return issubclass(type(obj), a_class) and type(obj) is not a_class
