from typing import Collection, TypeVar

_Tt = TypeVar("_Tt")


def sort(container: Collection[_Tt]) -> Collection[_Tt]:
	"""
	Sort input container with quick sort

	:param container: container of elements to be sorted
	:return: container sorted in ascending order
	"""
	if len(container) <= 1:
		return container
	low = []
	high = []
	equal = []
	base = container[0]
	for i in range(len(container)):
		if container[i] > base:
			high.append(container[i])
		elif container[i] < base:
			low.append(container[i])
		else:
			equal.append(container[i])
	low = sort(low)
	high = sort(high)
	return low + equal + high



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


