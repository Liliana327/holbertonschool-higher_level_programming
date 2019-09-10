#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
temporary = number
if number < 0:
    temporary = -number
string = temporary % 10
if number < 0:
    string = -string
print('Last digit of {:d} is {:d} '.format(number, string), end="")
if string > 5:
    print('and is greater than 5')
elif string == 0:
    print('and is 0')
else:
    print('and is less than 6 and not 0')
