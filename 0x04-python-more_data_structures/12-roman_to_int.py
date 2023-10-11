#!/usr/bin/python3
def roman_to_int(roman_string):
    if not isinstance(roman_string, str) or roman_string is None:
        return 0
    r_dict = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
    total = 0
    n = 0
    for r in reversed(roman_string):
        n = r_dict[r]
        total += n if total < n * 5 else -n
    return total
