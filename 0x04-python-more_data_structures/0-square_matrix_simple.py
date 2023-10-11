#!/usr/bin/python3

def square_matrix_simple(matrix=[]):
    newmatrix = []
    for li in matrix:
        newmatrix.append(list(map(lambda num: num * num, li)))
    return newmatrix
