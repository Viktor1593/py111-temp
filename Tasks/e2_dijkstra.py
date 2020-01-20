from typing import Hashable, Mapping, Union
import networkx as nx


def dijkstra_algo(g: nx.DiGraph, starting_node: Hashable) -> Mapping[Hashable, Union[int, float]]:
	"""
	Count shortest paths from starting node to all nodes of graph g
	:param g: Graph from NetworkX
	:param starting_node: starting node from g
	:return: dict like {'node1': 0, 'node2': 10, '3': 33, ...} with path costs, where nodes are nodes from g
	"""
	# print(g, starting_node)
	visited = []
	costs = {n: float('inf') for n in g.nodes()}
	costs[starting_node] = 0
	while True:
		node = min(filterTheDict(costs, lambda item: item[0] not in visited).items(), key=lambda x: x[1])[0]
		for n, val in g.adj[node].items():
			if costs[node] + val['weight'] < costs[n]:
				costs[n] = costs[node] + val['weight']
		visited.append(node)
		if len(visited) == len(g.nodes()):
			break

	print(g.adj)
	# print(costs)
	return costs

def filterTheDict(dictObj, callback):
    newDict = dict()
    # Iterate over all the items in dictionary
    for (key, value) in dictObj.items():
        # Check if item satisfies the given condition then add to new dict
        if callback((key, value)):
            newDict[key] = value
    return newDict

if __name__ == '__main__':
	G = nx.DiGraph()
	G.add_nodes_from("ABCDEFG")
	G.add_weighted_edges_from([
		("A", "B", 1),
		("B", "C", 3),
		("C", "E", 4),
		("E", "F", 3),
		("B", "E", 8),
		("C", "D", 1),
		("D", "E", 2),
		("B", "D", 2),
		("G", "D", 1),
		("D", "A", 2),
	])
	# print(dijkstra_algo(G, 'A')) # {'A': 0, 'B': 1, 'C': 4, 'D': 3, 'E': 5, 'F': 8, 'G': float("inf")}
	print(dijkstra_algo(G, 'D')) # {'A': 2, 'B': 3, 'C': 6, 'D': 0, 'E': 2, 'F': 5, 'G': float('inf')}
	# print(dijkstra_algo(G, 'G')) # {'A': 3, 'B': 4, 'C': 7, 'D': 1, 'E': 3, 'F': 6, 'G': 0}
