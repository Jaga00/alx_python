# This is a program that prints all possible different combinations of two digits.

for tens_digit in range(10):
    for units_digit in range(tens_digit + 1, 10):
        print(f"{tens_digit:2d}{units_digit:d}", end=",")

print()