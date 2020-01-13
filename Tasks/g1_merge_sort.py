from typing import Collection, TypeVar

_Tt = TypeVar("_Tt")

def merge(container, left, right):
	i = j = k = 0
	while i < len(left) and j < len(right):
		if left[i] < right[j]:
			container[k] = left[i]
			i += 1
		else:
			container[k] = right[j]
			j += 1
		k += 1

	while i < len(left):
		container[k] = left[i]
		i += 1
		k += 1

	while j < len(right):
		container[k] = right[j]
		j += 1
		k += 1
	return container

def sort(container: Collection[_Tt]) -> Collection[_Tt]:
	"""
	Sort input container with merge sort

	:param container: container of elements to be sorted
	:return: container sorted in ascending order
	"""

	if len(container) > 1:
		mid = len(container) // 2
		left = container[:mid]
		right = container[mid:]

		sort(left)
		sort(right)
		merge(container, left, right)
	return container


if __name__ == '__main__':
	import random
	N = 11
	sorted_list = list(range(N))
	random.shuffle(sorted_list)
	sorted_list = [6, 5, 12, 10, 9, 1]
	# sorted_list = [1, 0, 4, 2, 3]
	# sorted_list = [14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
	print(sorted_list)
	print(sort(sorted_list))