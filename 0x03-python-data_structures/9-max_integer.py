#!/usr/bin/python3
def max_integer(my_list=[]):
    if not my_list:
        return None
    sorted_list = my_list.copy()
    sorted_list.sort()
    return sorted_list[-1]
