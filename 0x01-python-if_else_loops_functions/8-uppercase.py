#!/usr/bin/python3
def uppercase(str):
    i = 0
    for char in str:
        if ord(char) in range(97, 123):
            char = chr(ord(char) - 32)
        if i != len(str):
            print("{}".format(char), end="")
        i += 1
    print("")
