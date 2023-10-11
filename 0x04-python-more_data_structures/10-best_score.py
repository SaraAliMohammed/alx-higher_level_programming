#!/usr/bin/python3

def best_score(a_dictionary):
    if not a_dictionary:
        return None
    max_v = 0
    max_k = ""
    for key,value in a_dictionary.items():
        if value > max_v:
            max_v = value
            max_k = key
    return max_k
