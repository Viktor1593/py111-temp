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
    index = None
    for i in array:
        if array[i] == find_elem:
            index = i
            break

    return index


if __name__ == '__main__':
    n = 1000
    array = np.arange(n)
    np.random.shuffle(array)

