from typing import Collection, TypeVar

_Tt = TypeVar("_Tt")


def sort(container: Collection[_Tt]) -> Collection[_Tt]:
	"""
	Sort input container with bubble sort

	:param container: container of elements to be sorted
	:return: container sorted in ascending order
	"""
	for i in range(len(container)):
		for j in range(len(container) - i - 1):
			if container[j] > container[j + 1]:
				container[j], container[j + 1] = container[j + 1], container[j]

	return container


if __name__ == '__main__':
	import random
	N = 10
	sorted_list = list(range(N))
	random.shuffle(sorted_list)
	print(sorted_list)
	print(sort(sorted_list))


