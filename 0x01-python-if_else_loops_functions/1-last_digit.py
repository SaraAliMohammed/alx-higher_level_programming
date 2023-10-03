#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
last_digit = int(str(number)[-1])
if number < 0:
    last_digit *= -1
print(
    "Last digit of {:d} is {:d} and is "
    .format(number, last_digit), end="")
if last_digit > 5:
    print("is greater than 5")
elif last_digit == 0:
    print("0")
elif last_digit < 6:
    print("less than 6 and not 0")
