#!/usr/bin/python3
"""This is My list Module"""


class MyList(list):
    """MyList class"""
    def print_sorted(self):
        """Prints the sorted array"""
        print(sorted(self))
