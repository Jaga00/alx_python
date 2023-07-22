# This is a program that prints all numbers from 0 to 98 in decimal and in hexadecimal

for num in range(99):
    print("{:2d} = 0x{:X}".format(num, num))