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
	return low + equal + high


