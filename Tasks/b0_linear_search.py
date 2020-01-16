"""
This module implements some functions based on linear search algo
"""
from typing import Sequence

import numpy

def min_search(arr: Sequence) -> int:
    """
    Function that find minimal element in array

    :param arr: Array containing numbers
    :return: index of first occurrence of minimal element in array
    """
    min = None
    mini = -1
    for i, elem in enumerate(arr):
        if min is None:
            min = elem
            mini = i
        elif elem < min:
            min = elem
            mini = i
    return mini


def find_elem(find_elem, array):
    for i, elem in enumerate(array):
        if elem == find_elem:
            return i

    return None


if __name__ == '__main__':
    n = 1000
    array = numpy.arange(n)
    numpy.random.shuffle(array)
    for _ in range(5):
        fe = numpy.random.choice(array)
        print(fe, find_elem(fe, array), sep=': ')