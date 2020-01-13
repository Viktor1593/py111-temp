from typing import Collection, TypeVar

_Tt = TypeVar("_Tt")


def sort(arr: Collection[_Tt]) -> Collection[_Tt]:
	"""
	Sort input container with merge sort

	:param container: container of elements to be sorted
	:return: container sorted in ascending order
	"""

	if len(arr) > 1:
		mid = len(arr) // 2  # Finding the mid of the array
		L = arr[:mid]  # Dividing the array elements
		R = arr[mid:]  # into 2 halves

		sort(L)  # Sorting the first half
		sort(R)  # Sorting the second half

		i = j = k = 0

		# Copy data to temp arrays L[] and R[]
		while i < len(L) and j < len(R):
			if L[i] < R[j]:
				arr[k] = L[i]
				i += 1
			else:
				arr[k] = R[j]
				j += 1
			k += 1

		# Checking if any element was left
		while i < len(L):
			arr[k] = L[i]
			i += 1
			k += 1

		while j < len(R):
			arr[k] = R[j]
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
	N = 4
	sorted_list = list(range(N))
	random.shuffle(sorted_list)
	# sorted_list = [1, 0, 4, 2, 3]
	# sorted_list = [14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
	print(sorted_list)
	print(sort(sorted_list))