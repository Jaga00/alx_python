# Positive and negative- program assigns a random signed number to the variable number each time it is executed

import random
number = random.randint(-10, 10)

if number > 0:
    print("{} is positive.".format(number))
elif number < 0:
    print("{} is negative.".format(number))
else:
    print("0 is zero.")

print()
