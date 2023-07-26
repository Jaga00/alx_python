# a function that raises a name exception with a message

class MyNameException(Exception):
    pass

def raise_exception_msg(message=""):
    try:
        raise MyNameException(message)
    except MyNameException as e:
        print(e)
        return

# Call the function
raise_exception_msg('James Okwemba')