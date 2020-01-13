from typing import Collection, TypeVar

_Tt = TypeVar("_Tt")

# http://sorting.at/
def sort(container: Collection[_Tt]) -> Collection[_Tt]:
	"""
	Sort input container with bubble sort

	:param container: container of elements to be sorted
	:return: container sorted in ascending order
	"""
	# n = 0
	for i in range(len(container)-1):
		k = 0
		for j in range(len(container) - i - 1):
			if container[j] > container[j + 1]:
				container[j], container[j + 1] = container[j + 1], container[j]
				k += 1
				# n += 1
		if k == 0:
			return container
		print('rotations: ', k)
	# print('rotations: n ', n)
	return container


if __name__ == '__main__':
	import random
	N = 5
	sorted_list = list(range(N))
	random.shuffle(sorted_list)
	# sorted_list = [1, 0, 4, 2, 3]
	# sorted_list = [14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
	print(sorted_list)
	print(sort(sorted_list))


