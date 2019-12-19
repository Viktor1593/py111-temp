from typing import Any, Sequence, Optional

import numpy


def binary_search(elem: Any, arr: Sequence) -> Optional[int]:
	"""
	Performs binary search of given element inside of array

	:param elem: element to be found
	:param arr: array where element is to be found
	:return: Index of element if it's presented in the arr, None otherwise
	"""

	ln = len(arr) // 2
	ind = ln

	for i in range(ln):
		print(ln, ind, sep=': ')
		if arr[ind] == elem:
			return ind
		if ln == 1:
			break
		ln = ln / 2
		iln = int(ln)
		print(ln - iln)
		if ln - iln == 0.5:
			ln = iln + 1
		else:
			ln = iln

		if ln == 0:
			ln = 1
		if arr[ind] > elem:
			ind -= ln
		else:
			ind += ln
	# print(elem, arr)
	return None

if __name__ == '__main__':
	n = 125
	arr = []
	for i in range(n):
		arr.append(numpy.random.randint(i, n))
	arr = numpy.sort(arr)
	arr = numpy.unique(arr)
	# array = numpy.arange(n)
	# numpy.random.shuffle(array)
	print(arr)
	print('found: ', binary_search(75, arr))
