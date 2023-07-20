# function called fibonacci_sequence that takes a number n as input and returns a list of the first n Fibonacci numbers.

def fibonacci_sequence(n):
    if n <= 0:
        return []

    sequence = [0, 1]

    for i in range(2, n):
        next_number = sequence[-1] + sequence[-2]
        sequence.append(next_number)

    return sequence[:n]