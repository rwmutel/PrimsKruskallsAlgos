"""
Prim's algorithm here.
"""
import random
import networkx as nx


def prims_algo(nxgraph: nx.Graph) -> int:
    data = list(nxgraph.edges.data())

    visited = list()
    unvisited = list(nxgraph.nodes)
    num_of_nodes = len(unvisited)

    starting_edge = random.choice(unvisited)

    visited.append(starting_edge)
    unvisited.remove(starting_edge)

    carcass_weight = 0

    while len(visited) < num_of_nodes:
        minimum = 10000000
        best_visit = 10000000
        for node in visited:
            for unv_node in unvisited:
                for element in data:
                    if node in element:
                        if unv_node in element:
                            if minimum > int(element[2]["weight"]):
                                minimum = element[2]["weight"]
                                best_visit = unv_node
        carcass_weight += minimum
        unvisited.remove(best_visit)
        visited.append(best_visit)
    return carcass_weight
