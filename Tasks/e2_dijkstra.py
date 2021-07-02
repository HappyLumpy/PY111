from typing import Hashable, Mapping, Union
import networkx as nx
from collections import deque
import matplotlib


def dijkstra_algo(g: nx.DiGraph, starting_node: Hashable) -> Mapping[Hashable, Union[int, float]]:
    """
    Count shortest paths from starting node to all nodes of graph g
    :param g: Graph from NetworkX
    :param starting_node: starting node from g
    :return: dict like {'node1': 0, 'node2': 10, '3': 33, ...} with path costs, where nodes are nodes from g
    """
    queue = deque()
    s = {starting_node: 0}
    queue.append(starting_node)
    while queue:
        v = queue.pop()
        for u in g[v]:
            if u not in s or s[v] + g[v][u]['weight'] < s[u]:
                s[u] = s[v] + g[v][u]['weight']
                queue.append(u)
    return s


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
    print(dijkstra_algo(G, "A"))
    nx.draw(G)
# {'A': 3, 'B': 4, 'C': 7, 'D': 1, 'E': 3, 'F': 6, 'G': 0}
