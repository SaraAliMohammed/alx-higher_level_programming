#!/usr/bin/python3
def uppercase(str):
    i = 0
    if str != "":
        for char in str:
            i += 1
            if ord(char) in range(97, 123):
                char = chr(ord(char) - 32)
            if i != len(str):
                print("{}".format(char), end="")
            else:
                print("{}".format(char))
