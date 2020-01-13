from typing import Collection, TypeVar

_Tt = TypeVar("_Tt")


def sort(arr: Collection[_Tt]) -> Collection[_Tt]:
	"""
	Sort input container with merge sort

	:param container: container of elements to be sorted
	:return: container sorted in ascending order
	"""

	if len(arr) > 1:
		mid = len(arr) // 2
		left = arr[:mid]
		right = arr[mid:]

		sort(left)
		sort(right)

		i = j = k = 0

		while i < len(left) and j < len(right):
			if left[i] < right[j]:
				arr[k] = left[i]
				i += 1
			else:
				arr[k] = right[j]
				j += 1
			k += 1

		while i < len(left):
			arr[k] = left[i]
			i += 1
			k += 1

		while j < len(right):
			arr[k] = right[j]
			j += 1
			k += 1
	return arr
	# if len(container) <= 1:
	# 	return container
	# middle = len(container) // 2
	# print(middle)
	# left = sort(container[:middle])
	# right = sort(container[middle:])
	# res = []
	# i = j = k = 0
	# res = []
	# while i < len(left) and j < len(right):
	# 	if left[i] < right[j]:
	# 		res.append(left[i])
	# 		i += 1
	# 	else:
	# 		res.append(right[j])
	# 		j += 1
	#
	# 	while i < len(left):
	# 		res.append(left[i])
	# 		i += 1
	# 		k += 1
	#
	# 	while j < len(right):
	# 		res.append(right[j])
	# 		j += 1
	# 		k += 1
	#
	# return res
	# middle = length(m) / 2
	# 	for each x in m up to middle
	# 	add
	# 	x
	# 	to
	# 	left
	# for each x in m after middle
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
	# return container


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