# a function that removes all characters c and C from a string.

def no_c(my_string):
    result = ""
    for char in my_string:
        if char not in ('c', 'C'):
            result += char
    return result