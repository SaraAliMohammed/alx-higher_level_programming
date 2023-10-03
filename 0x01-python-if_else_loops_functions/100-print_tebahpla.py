#!/usr/bin/python3
for character in range(122, 96, -2):
    print(
        "{}{}".format(chr(character), chr(character-33)), end="")
