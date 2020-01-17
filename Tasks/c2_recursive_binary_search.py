from typing import Any, Sequence, Optional


def binary_search(elem: Any, arr: Sequence, l = 0, h = None) -> Optional[int]:
	"""
	Performs binary search of given element inside of array (using recursive way)

	:param elem: element to be found
	:param arr: array where element is to be found
	:return: Index of element if it's presented in the arr, None otherwise
	"""
	if h is None:
		h = len(arr)-1
	if h >= l:
		mid = l + (h-l)//2
		if arr[mid] == elem: 
			return mid 
		elif arr[mid] > elem: 
			return binary_search(elem, arr, l, mid-1) 
		else: 
			return binary_search(elem, arr, mid+1, h)
	else: 
		return None

if __name__ == '__main__':
	arr = [i for i in range(100)] + [101]
	print(binary_search(5, arr))
	print(binary_search(54, arr))

	print(binary_search(-1, arr))
	print(binary_search(100, arr))

	print(binary_search(0, arr))
	print(binary_search(101, arr))