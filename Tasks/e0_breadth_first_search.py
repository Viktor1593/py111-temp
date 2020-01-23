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
	path = []
	nodes_queue = deque()
	nodes_queue.appendleft(start_node)
	path.append(start_node)
	while True:
		node = nodes_queue.pop()
		for n in g.adj[node]:
			if n not in path:
				path.append(n)
				nodes_queue.appendleft(n)
		if len(nodes_queue) == 0:
			break
	return path


def bfs_find(graph, src, dst):
	visited = {node: False for node in graph.nodes()}
	parents = {src: src}

	deque_nodes = deque()
	deque_nodes.appendleft(src)
	while True:
		try:
			src = deque_nodes.pop()
			visited[src] = True
			for node in graph.adj[src]:
				if not visited[node]:
					deque_nodes.append(node)
					parents[node] = parents[src] + node
				if node == dst:
					return parents[node]
		except IndexError:
			return None


if __name__ == '__main__':
	graph = nx.Graph()
	graph.add_nodes_from("ABCDEFGHIJ")
	graph.add_edges_from([
		('A', 'B'),
		('A', 'F'),
		('B', 'G'),
		('F', 'G'),
		('G', 'C'),
		('G', 'H'),
		('G', 'I'),
		('C', 'H'),
		('I', 'H'),
		('H', 'D'),
		('H', 'E'),
		('H', 'J'),
		('E', 'D'),
	])
	result = bfs(graph, 'A')
	print(graph.adj)
	print(result) #ABFGCHIDEJ

	# src = 'A'
	# dst = 'G'
	# graph.add_node('Z')
	# # print(graph.adj)
	# print(bfs_find(graph, src, dst))

