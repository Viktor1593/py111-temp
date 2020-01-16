from typing import Any, Sequence, Optional

import numpy
import time


def binary_search(elem: Any, arr: Sequence) -> Optional[int]:
    """
    Performs binary search of given element inside of array
    :param elem: element to be found
    :param arr: array where element is to be found
    :return: Index of element if it's presented in the arr, None otherwise
    """

    # print(elem, arr)

    l = 0
    h = len(arr)-1
    while l <= h:
        # print(l, h, sep=': ')
        mid = (l + h) // 2
        if elem < arr[mid]:
            h = mid - 1
        elif elem > arr[mid]:
            l = mid + 1
        else:
            return mid
    return None


def find_elem(find_elem, array):
    for i, elem in enumerate(array):
        if elem == find_elem:
            return i

    return None
	
if __name__ == '__main__':
    ns = [10, 100, 1000, 10000, 100000]
    for n in ns:
        arr = []
        for i in range(n):
            arr.append(numpy.random.randint(0, n))
        arr = numpy.unique(arr)
        st = time.time()
        arr = numpy.sort(arr)
        to_search = numpy.random.randint(0, n)
        print('found: ', binary_search(to_search, arr))
        print(time.time() - st)


        arr = []
        for i in range(n):
            arr.append(numpy.random.randint(0, n))
        arr = numpy.unique(arr)
        st = time.time()
        print('found: ', find_elem(to_search, arr))
        print(time.time() - st)