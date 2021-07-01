from typing import Hashable, List
import networkx as nx


def dfs(g: nx.Graph, start_node: Hashable, used = None) -> List[Hashable]:
    """
    Do an depth-first search and returns list of nodes in the visited order

    :param g: input graph
    :param start_node: starting node of search
    :return: list of nodes in the visited order
    """
    if used is None:
        used = []
    used.append(start_node)
    for neighbor in g[start_node]:
        if neighbor not in used:
            dfs(g, neighbor, used)
    return used


if __name__ == '__main__':
    graph = nx.Graph()
    graph.add_nodes_from("ABCDEFG")
    graph.add_edges_from([
        ('A', 'B'),
        ('A', 'C'),
        ('B', 'D'),
        ('B', 'E'),
        ('C', 'F'),
        ('E', 'G'),
    ])
    print(dfs(graph,'A'))

    list('ABDEGCF'),
    list('ABEGDCF'),
    list('ACFBDEG'),
    list('ACFBEGD')