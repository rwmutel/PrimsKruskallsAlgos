"""
Prim's algorithm here.
"""
import random
import networkx as nx


def prims_algo(nxgraph: nx.Graph) -> int:
    data = list(nxgraph.edges.data())

    visited = set()
    unvisited = set()

    for node in nxgraph.nodes:
        unvisited.add(node)

    num_of_nodes = len(unvisited)
    starting_edge = random.choice(list(unvisited))

    visited.add(starting_edge)
    unvisited.remove(starting_edge)

    adjacency = tuple(nxgraph.adjacency())

    num_of_visited = 1
    carcass_weight = 0

    while num_of_visited < num_of_nodes:
        minimum = float("inf")
        best_choice = -1
        for node in range(num_of_nodes):
            if node in visited:
                for unv_node in unvisited:
                    if unv_node in adjacency[node][1]:
                        if minimum > adjacency[node][1][unv_node]["weight"]:
                            minimum = adjacency[node][1][unv_node]["weight"]
                            best_choice = unv_node

        num_of_visited += 1
        carcass_weight += minimum
        unvisited.remove(best_choice)
        visited.add(best_choice)

    return carcass_weight
