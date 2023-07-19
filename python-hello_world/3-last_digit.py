# Last digit- program assigns a random signed number to the variable number each time it is executed

import random
number = random.randint(-10000, 10000)

Last_digit = (number) % 10

print("Last digit of {} is {},".format(number, Last_digit))

if Last_digit > 5:
    print("and is greater than 5")
elif Last_digit < 6:
    print("and is less than 6 and not 0")
else:
    print("and is 0")

print("\n")