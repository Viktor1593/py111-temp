"""
Priority Queue

Queue priorities are from 0 to 5
"""
from typing import Any

import random


my_prio_queue = {}

def enqueue(elem: Any, priority: int = 0) -> None:
	"""
	Operation that add element to the end of the queue

	:param elem: element to be added
	:return: Nothing
	"""
	global my_prio_queue
	# priority = str(priority)
	if priority not in my_prio_queue:
		my_prio_queue[priority] = []
	my_prio_queue[priority].append(elem)
	return None

def get_max_prio():
	global my_prio_queue
	p = None
	for p_i, q in enumerate(my_prio_queue):
		# print(p_i, q, sep = ": ")
		if len(my_prio_queue[q]) > 0:
			if p is None:
				p = q
			if q < p:
				p = q
	return p


def dequeue() -> Any:
	"""
	Return element from the beginning of the queue

	:return: dequeued element
	"""
	global my_prio_queue
	prio = get_max_prio()
	if prio is None:
		return None
	deq = my_prio_queue[prio][0]
	del my_prio_queue[prio][0]
	return deq


def peek(ind: int = 0, priority: int = 0) -> Any:
	"""
	Allow you to see at the element in the queue without dequeuing it

	:param ind: index of element (count from the beginning)
	:return: peeked element
	"""
	global my_prio_queue
	if priority in my_prio_queue.keys():
		return my_prio_queue[priority][ind]
	return None


def clear() -> None:
	"""
	Clear my queue

	:return: None
	"""
	global my_prio_queue
	my_prio_queue = {}
	return None

if __name__ == '__main__':
	for i in range(10):
		enqueue(i, random.randint(0, 5))
	print(my_prio_queue)
	
	for i in range(10):
		print(dequeue())
		
