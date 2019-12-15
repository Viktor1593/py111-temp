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
    global my_stack
    my_stack.append(elem)
    # print(elem)
    return None


def pop() -> Any:
  """
  Pop element from the top of the stack
	:param elem: element to be pushed
	:return: Nothing
	"""
	global my_stack
	my_stack.append(elem)
	print(elem)
	return None


def pop() -> Any:
	"""
	Pop element from the top of the stack

	:return: popped element
	"""
	global my_stack
	pop_elem = my_stack[-1]
	del my_stack[-1]
	return pop_elem


def peek(ind: int = 0) -> Any:
    """
    Allow you to see at the element in the stack without popping it

    :param ind: index of element (count from the top)
    :return: peeked element
    """
    global my_stack
    ind = ind % len(my_stack)
    # print(my_stack[ind])
    return my_stack[-ind-1]


def clear() -> None:
    """
    Clear my stack

    :return: None
    """
    global my_stack
    my_stack = []
    return None


if __name__ == '__main__':
    print('test push')
    for i in range(10):
        push(i)
    # print('test peek')
    # for i in range(10):
    #     peek(i)
    # print('test pop')
    # for i in range(15):
    #     pop()
    clear()
    print(my_stack)
