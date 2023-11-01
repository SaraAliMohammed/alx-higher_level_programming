#!/usr/bin/python3
"""
Multiplies 2 matricies using numpy module
"""
import numpy


def lazy_matrix_mul(m_a, m_b):
    """
    multiplies 2 matrices by using the module NumPy
    Args:
        m_a: the first matrix
        m_b: the second matrix
    Returns:
        return m_a * m_b
    """
    return numpy.matmul(m_a, m_b)
