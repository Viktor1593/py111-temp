"""
My little Stack
"""
from typing import Any

my_stack = []
def push(elem: Any) -> None:
	"""
	Operation that add element to stack

	:param elem: element to be pushed
	:return: Nothing
	"""
	my_stack.append(elem)
	print(elem)
	return None


def pop() -> Any:
	"""
	Pop element from the top of the stack

	:return: popped element
	"""
	pop_elem = my_stack[-1]
	del my_stack[-1]
	return pop_elem



def peek(ind: int = 0) -> Any:
	"""
	Allow you to see at the element in the stack without popping it

	:param ind: index of element (count from the top)
	:return: peeked element
	"""
	# print(ind)
	if ind > len(my_stack):
		print('overflow')
	else:
		return my_stack[-ind-1]


def clear() -> None:
	"""
	Clear my stack

	:return: None
	"""
	my_stack = []
	return None


if __name__ == '__main__':
	my_stack = [1, 2]
	push(3)
	print(my_stack)
	print(pop())
	print(my_stack)
	print(peek(0))
	print(peek(1))
	print(peek(10))

