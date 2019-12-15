"""
My little Queue
"""
from typing import Any

my_queue = []
def enqueue(elem: Any) -> None:
	"""
	Operation that add element to the end of the queue

	:param elem: element to be added
	:return: Nothing
	"""
	global my_queue
	my_queue.append(elem)
	print(elem)
	return None


def dequeue() -> Any:
	"""
	Return element from the beginning of the queue

	:return: dequeued element
	"""
	global my_queue
	if len(my_queue) == 0:
		return None
	else:
		deq = my_queue[0]
		del my_queue[0]
		return deq


def peek(ind: int = 0) -> Any:
	"""
	Allow you to see at the element in the queue without dequeuing it

	:param ind: index of element (count from the beginning)
	:return: peeked element
	"""
	global my_queue
	print(ind)
	return my_queue[ind]


def clear() -> None:
	"""
	Clear my queue

	:return: None
	"""
	global my_queue
	my_queue = []
	return None
