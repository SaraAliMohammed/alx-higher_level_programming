#!/usr/bin/python3
def remove_char_at(str, n):
    if n >= len(str) or n < 0:
        return str
    if n == 0:
        return str[1:]
    return str[0] + remove_char_at(str[1:], n - 1)
