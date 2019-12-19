from typing import Any, Sequence, Optional

import numpy


def binary_search(elem: Any, arr: Sequence) -> Optional[int]:
    """
    Performs binary search of given element inside of array

    :param elem: element to be found
    :param arr: array where element is to be found
    :return: Index of element if it's presented in the arr, None otherwise
    """

    print(elem, arr)
    l = 0
    h = len(arr)-1
    while l <= h:
        print(l, h, sep=': ')
        mid = (l + h) // 2
        if elem < arr[mid]:
            h = mid - 1
        elif elem > arr[mid]:
            l = mid + 1
        else:
            return mid
    return None


if __name__ == '__main__':
    n = 125
    arr = []
    for i in range(n):
        arr.append(numpy.random.randint(i, n))
    arr = numpy.unique(arr)
    arr = numpy.sort(arr)

    # arr = list(range(100))
    # array = numpy.arange(n)
    # numpy.random.shuffle(array)
    # print(arr)
    print('found: ', binary_search(99, arr))
