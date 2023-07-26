#  a function that divides 2 integers and prints the result

def safe_print_division(a, b):
    try:
        result = a / b
    except ZeroDivisionError:
        return None
    else:
        return result
    finally:
        print("Inside result: {}".format(result) if 'result' in locals() else "Inside result: None")
