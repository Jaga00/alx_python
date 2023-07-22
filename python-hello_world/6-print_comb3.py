# This is a program that prints all possible different combinations of two digits.

combination_list = []

for tens_digit in range(10):
    for units_digit in range(tens_digit + 1, 10):
        combination_list.append("{:2d}{:d}".format(tens_digit,units_digit))

output = ",".join(combination_list)
print(output)