# function that computes a to the power of b and return the value.

def pow(a, b):
    result = 1

    for _ in range(b):
        result *= a

    return result