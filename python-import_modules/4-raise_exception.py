#  a function that raises a type exception.

class MyTypeException(Exception):
    pass

def raise_exception(message="Exception has been raised"):
    try:
        raise MyTypeException(message)
    except MyTypeException as e:
        print(e)
        return
