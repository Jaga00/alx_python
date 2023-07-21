# function that computes a to the power of b and return the value.

def pow(a, b):
    if b == 0:
        return 1
    elif b < 0:
        return 1 / pow(a, -b)
    else:
        result = 1
        for _ in range(b):
            result *= a
        return result
    