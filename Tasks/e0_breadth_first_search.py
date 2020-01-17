from typing import Hashable, List
import networkx as nx
from collections import deque

def bfs(g: nx.Graph, start_node: Hashable) -> List[Hashable]:
	"""
	Do an breadth-first search and returns list of nodes in the visited order

	:param g: input graph
	:param start_node: starting node for search
	:return: list of nodes in the visited order
	"""
	print(g, start_node)
	return list(g.nodes)


def bfs_find(graph, src, dst):
	'''

	:param graph:
	:param src:
	:param dst:
	:param visited:
	:return:
	'''
	visited = []
	nodes_queue = deque()
	nodes_queue.appendleft(src)
	# while True:
	# 	for node in graph.adj[src]:
	# 		if not node in visited:
	# 			visited.append(src)
	# 			if node == src:
	# 				return visited
					

	if not src in visited:
		visited.append(src)
	# visited[src] = True
	if src == dst:
		return True
	for node in graph.adj[src]:
		if not node in visited:
		# if not visited[node]:
			if dfs_find(graph, node, dst, visited):
				return True
	return False


if __name__ == '__main__':
	graph = nx.Graph()
	graph.add_nodes_from("ABCDEFG")
	graph.add_edges_from(
		[
			('A', 'B'),
			('A', 'C'),
			('B', 'D'),
			('B', 'E'),
			('C', 'F'),
			('E', 'G')
		]
	)
	start = 'A'
	dst = 'G'
	graph.add_node('Z')
	# print(graph.adj)
	print(dfs_find(graph, start, dst, visited))

