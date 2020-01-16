def fib_recursive(n: int) -> int:
	"""
	Calculate n-th number of Fibonacci sequence using recursive algorithm

	:param n: number of item
	:return: Fibonacci number
	"""
	if n < 0:
		raise ValueError
	elif n == 1:
		return 1
	elif n == 2:
		return 1
	else:
		return fib_recursive(n-1) + fib_recursive(n-2)


def fib_iterative(n: int) -> int:
	"""
	Calculate n-th number of Fibonacci sequence using iterative algorithm

	:param n: number of item
	:return: Fibonacci number
	"""
	# print(n)
	if n < 0:
		raise ValueError
	a, b = 0, 1
	for _ in range(n-1):
		a, b = b, a + b
	return b


if __name__ == '__main__':
	print(fib_recursive(8)) #21
	print(fib_iterative(9)) #34
