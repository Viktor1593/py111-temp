from typing import Collection, TypeVar

_Tt = TypeVar("_Tt")


def sort(container: Collection[_Tt]) -> Collection[_Tt]:
	"""
	Sort input container with merge sort

	:param container: container of elements to be sorted
	:return: container sorted in ascending order
	"""
	if len(container) <= 1:
		return container
	middle =


	# 		middle = length(m) / 2
	# 		for each x in m up to middle
	# 		add
	# 		x
	# 		to
	# 		left
	# 	for each x in m after middle
	# 	add
	# 	x
	# 	to
	# 	right
	#
	#
	# left = mergesort(left)
	# right = mergesort(right)
	# result = merge(left, right)
	# return result

	return container


if __name__ == '__main__':
