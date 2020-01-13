from typing import Collection, TypeVar

_Tt = TypeVar("_Tt")


def sort(container: Collection[_Tt]) -> Collection[_Tt]:
	"""
	Sort input container with bubble sort

	:param container: container of elements to be sorted
	:return: container sorted in ascending order
	"""
	return container


if __name__ == '__main__':
	import random
	N = 10
	sorted_list = list(range(N))
	sorted_list = random.shuffle(sorted_list)
	print(sorted_list)


