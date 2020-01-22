"""
You can do it either with networkx ('cause tree is a graph)
or with dicts (smth like {'key': 0, value: 123, 'left': {...}, 'right':{...}})
"""

from typing import Hashable, Any, Optional, Tuple
# import networkx as nx


b_tree = {}

def recurcive_insert(key: Hashable, value: Any, branch: dict) -> Any:
	"""
	recurcive Insert (key, value) pair to binary search tree

	:param key: key from pair (key is used for positioning node in the tree)
	:param value: value associated with key
	:param branch: current branch
	:return: None
	"""
	if branch == {}:
		return {'key': key, 'value': value, 'left': {}, 'right': {}}
	elif branch['key'] > key:
		return {
			'key': branch['key'], 
			'value': branch['value'], 
			'left': recurcive_insert(key, value, branch['left']), 
			'right': branch['right']
		}
	elif branch['key'] < key:
		return {
			'key': branch['key'], 
			'value': branch['value'],
			'left': branch['left'], 
			'right': recurcive_insert(key, value, branch['right'])
		}
	else:
		return {
			'key': branch['key'], 
			'value': value,
			'left': branch['left'], 
			'right': branch['right']
		}

def insert(key: Hashable, value: Any) -> None:
	"""
	Insert (key, value) pair to binary search tree

	:param key: key from pair (key is used for positioning node in the tree)
	:param value: value associated with key
	:return: None
	"""
	global b_tree
	b_tree = recurcive_insert(key, value, b_tree)
	# print(key, value)
	# print(b_tree)
	return None


def get_min(branch: dict) -> Optional[Any]:
	"""
	recurcive searcing of min value

	:param branch: current branch
	:return: found node
	"""
	if len(branch.items()) == 0:
		return {}
	if branch['left'] == {} and branch['right'] == {}:
		return branch
	elif len(branch['left'].items()) > 0:
		return get_min(branch['left'])
	else:
		return get_min(branch['right'])
	return None

def re_recurcive(key: Hashable, branch: dict) -> None:
	"""
	recursive remove key and associated value from the BST if exists

	:param key: key to be removed
	:param branch: current branch
	:return: deleted (key, value) pair or None
	"""
	if len(branch.items()) == 0:
		return {}
	elif branch['key'] > key:
		return {
			'key': branch['key'], 
			'value': branch['value'], 
			'left': re_recurcive(key, branch['left']), 
			'right': branch['right']
		}
	elif branch['key'] < key:
		return {
			'key': branch['key'], 
			'value': branch['value'],
			'left': branch['left'], 
			'right': re_recurcive(key, branch['right'])
		}
	else:
		if branch['left'] == {} and branch['right'] == {}:
			return branch
		elif len(branch['left'].items()) > 0 and len(branch['right'].items()) > 0:
			min_node = get_min(branch['right'])
			if len(min_node.items()) > 0:
				remove(min_node['key'])
			else:
				return branch
		elif len(branch['left'].items()) > 0:
			return branch['left']
		else:
			return branch['right']




def remove(key: Hashable) -> Optional[Tuple[Hashable, Any]]:
	"""
	Remove key and associated value from the BST if exists

	:param key: key to be removed
	:return: deleted (key, value) pair or None
	"""
	global b_tree
	b_tree = re_recurcive(key, b_tree)
	# print(b_tree)
	return None


def find(key: Hashable) -> Optional[Any]:
	"""
	Find value by given key in the BST

	:param key: key for search in the BST
	:return: value associated with the corresponding key
	"""
	
	global b_tree
	c_branch = b_tree
	while True:
		if c_branch == {}:
			raise KeyError
		elif c_branch['key'] == key:
			return c_branch['value']
		elif c_branch['key'] > key:
			c_branch = c_branch['left']
		else:
			c_branch = c_branch['right']
	# print(key)
	return None
 

def clear() -> None:
	"""
	Clear the tree

	:return: None
	"""
	
	global b_tree
	b_tree = {}
	return None

if __name__ == '__main__':
	insert(42, 'The meaning of life, the universe and everything.')
	insert(0, 'ZERO!')
	insert(13, "Devil's sign here")
	insert(13, "Oh no, devil's sign again Oo")
	insert(42, "The meaning again")
	insert(42, "Predictable")
	insert(13, "And again")
	insert(-999, "Nobody expects spanish inquisition!")
	insert(0, "Never")
	insert(1, "gonna")
	insert(2, "give")
	insert(11, "you")
	insert(-3, "up")
	remove(42)
	remove(42)
	remove(43)
	remove(13)
	find(13)
	find(100)
