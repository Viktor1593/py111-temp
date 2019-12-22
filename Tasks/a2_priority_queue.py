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


def dequeue() -> Any:
	"""
	Return element from the beginning of the queue

	:return: dequeued element
	"""
	global my_prio_queue
	cur_prio = 0
	
	for prio in my_prio_queue:
		if prio > cur_prio and len(my_prio_queue[prio]) > 0:
			cur_prio = prio
	if cur_prio in my_prio_queue:
		if 0 in my_prio_queue[cur_prio]:
			deq = my_prio_queue[cur_prio][0]
			del my_prio_queue[cur_prio][0]
			return deq
	return None


def peek(ind: int = 0, priority: int = 0) -> Any:
	"""
	Allow you to see at the element in the queue without dequeuing it

	:param ind: index of element (count from the beginning)
	:return: peeked element
	"""
	global my_prio_queue
	if priority in my_prio_queue:
		if ind in my_prio_queue[priority]:
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
		
