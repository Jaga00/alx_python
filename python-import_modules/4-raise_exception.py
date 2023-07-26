#  a function that raises a type exception.

class MyTypeException(Exception):
    pass

def raise_exception(message=""):
    try:
        raise MyTypeException(message)
    except MyTypeException as e:
        print(e)
        return

# Call the function
raise_exception("Type exception")