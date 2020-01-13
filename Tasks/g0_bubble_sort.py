from typing import Collection, TypeVar

_Tt = TypeVar("_Tt")

# http://sorting.at/
def sort(container: Collection[_Tt]) -> Collection[_Tt]:
	"""
	Sort input container with bubble sort

	:param container: container of elements to be sorted
	:return: container sorted in ascending order
	"""
	for i in range(len(container)-1):
		for j in range(len(container) - i - 1):
			if container[j] > container[j + 1]:
				container[j], container[j + 1] = container[j + 1], container[j]

	return container


if __name__ == '__main__':
	import random
	N = 5
	sorted_list = list(range(N))
	random.shuffle(sorted_list)
	# # sorted_list = [1, 0, 4, 2, 3]
	# sorted_list = [4, 3, 2, 1, 0]
	print(sorted_list)
	print(sort(sorted_list))


