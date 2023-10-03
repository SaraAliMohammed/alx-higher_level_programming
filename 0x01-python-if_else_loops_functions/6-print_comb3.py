#!/usr/bin/python3
for number1 in range(0, 10):
    for number2 in range(number1 + 1, 10):
        if number1 != number2:
            print("{:d}{:d}".format(number1, number2), end="")
            if number1 != 8:
                print("", end=", ")
            else:
                print()
