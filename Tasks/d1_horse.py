

def calculate_paths(shape: (int, int), point: (int, int)) -> int:
	"""
	Given field with size rows*cols count available paths from (0, 0) to point

	:param shape: tuple of rows and cols (each from 1 to rows/cols)
	:param point: desired point for horse
	:return: count of paths from (1, 1) to (point[0], point[1]) (numerating from 0, so (0, 0) - left bottom tile)
	"""
	# print(point, shape)
	# print(not (point[0] in list(range(shape[0]))) and (point[1] in list(range(shape[1]))))
	# print(len(visited))
	if not ((point[0] in range(shape[0])) and (point[1] in range(shape[1]))):
		return 0
	elif point == (1, 1):
		return 1
	else:
		pass
		# res1 = calculate_paths(shape, (point[0] + 1, point[1] + 2))
		res2 = calculate_paths(shape, (point[0] + 1, point[1] - 2))
		res3 = calculate_paths(shape, (point[0] - 1, point[1] - 2))
		# res4 = calculate_paths(shape, (point[0] - 1, point[1] + 2))
		# res5 = calculate_paths(shape, (point[0] + 2, point[1] + 1))
		# res6 = calculate_paths(shape, (point[0] + 2, point[1] - 1))
		res7 = calculate_paths(shape, (point[0] - 2, point[1] + 1))
		res8 = calculate_paths(shape, (point[0] - 2, point[1] - 1))
		# return res1 + res2 + res3 + res4 + res5 + res6 + res7 + res8
		return res2 + res3 + res7 + res8

if __name__ == '__main__':

	print(calculate_paths((8, 8), (7, 7)))
	# print(calculate_paths((9, 9), (8, 8)))
	# print(calculate_paths((17, 12), (16, 9)))
	# print(calculate_paths((12, 10), (11, 9)))