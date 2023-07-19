# Positive and negative- program assigns a random signed number to the variable number each time it is executed

import random
number = random.randint(-10, 10)

if number > 0:
    print("The number {} is positive.".format(number))
elif number < 0:
    print("The number {} is negative.".format(number))
else:
    print("The number is zero.")

print()
