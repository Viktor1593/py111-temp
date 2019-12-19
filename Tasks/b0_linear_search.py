"""
This module implements some functions based on linear search algo
"""
from typing import Sequence
import random

import numpy

def min_search(arr: Sequence) -> int:
    """
    Function that find minimal element in array

    :param arr: Array containing numbers
    :return: index of first occurrence of minimal element in array
    """
    print(arr)
    return -1


def find_elem(find_elem, array):
    for i, elem in enumerate(array):
        if elem == find_elem:
            return i

    return None


if __name__ == '__main__':
    n = 1000
    array = numpy.arange(n)
    numpy.random.shuffle(array)
    print(find_elem(50, array))

