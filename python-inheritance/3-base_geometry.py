'''
 an empty class BaseGeometry.
'''

class BaseGeometry:
    """
    BaseGeometry class serves as a base for geometry classes.
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