# a function that computes the square value of all integers of a matrix.

def square_matrix_simple(matrix=[]):
    # Create a new matrix to store the squared values
    result_matrix = []
    for row in matrix:
        # Initialize a new row for the result matrix
        new_row = []
        for element in row:
            # Compute the square value of each element and append to the new row
            new_row.append(element ** 2)
        # Append the new row to the result matrix
        result_matrix.append(new_row)
    return result_matrix


