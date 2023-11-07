#!/usr/bin/python3
"""This is Pascal's Triangle Module """


def pascal_triangle(n):
    """
    Args:
        n: An integer.
    Returns: A list of lists of integers representing the
        Pascal’s triangle of n.
    """
    if n < 0:
        return []
    ps_triangles = [[1]]
    while len(ps_triangles) != n:
        triangle = pascal_triangles[-1]
        temp = [1]
        for i in range(len(triangle) - 1):
            temp.append(triangle[i] + triangle[i + 1])
        temp.append(1)
        ps_triangles.append(temp)
    return ps_triangles
