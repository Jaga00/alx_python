# a function that prints a matrix of integers.s

def print_matrix_integer(matrix=[[]]):
    for row in matrix:
        for element in row:
            print("{:d}".format(element), end=" ")
        print()

