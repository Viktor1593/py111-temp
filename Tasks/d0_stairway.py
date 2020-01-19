from typing import Union, Sequence


def stairway_path(stairway: Sequence[Union[float, int]]) -> Union[float, int]:
	"""
	Calculate min cost of getting to the top of stairway if agent can go on next or through one step.

	:param stairway: list of ints, where each int is a cost of appropriate step
	:return: minimal cost of getting to the top
	"""
	last_i = len(stairway) - 1
	# print(last_i)
	if last_i < 0:
		return 0
	elif last_i == 0:
		return stairway[0]
	else:
		res1 = stairway[last_i] + stairway_path(stairway[:(last_i)])
		res2 = stairway[last_i] + stairway_path(stairway[:(last_i-1)])
		if res1 < res2:
			return res1
		else:
			return res2


if __name__ == '__main__':
	test_st = [1, 3, 1, 5, 2, 7, 7, 8, 9, 4, 6, 3]
	# last_i = len(test_st) - 1
	# print(test_st[:last_i])
	# print(test_st[:last_i-1])
	print(stairway_path(test_st))
	test_st = [4, 4, 3, 2, 3, 4, 5, 9, 1, 2, 4, 2]
	print(stairway_path(test_st))
	test_st = [5, 11, 43, 2, 23, 43, 22, 12, 6, 8]
	print(stairway_path(test_st))
	test_st = [4, 12, 32, 22, 1, 7, 0, 12, 4, 2, 2]
	print(stairway_path(test_st))