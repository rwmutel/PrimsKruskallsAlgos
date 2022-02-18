"""
Prim's algorithm here.
"""
import random
import networkx as nx
from main import gnp_random_connected_graph


def prims_algo(graph: nx.Graph) -> int:
    data = list(graph.edges.data())

    visited = list()
    unvisited = list(graph.nodes)
    num_of_nodes = len(unvisited)

    starting_edge = random.choice(unvisited)

    visited.append(starting_edge)
    unvisited.remove(starting_edge)

    carcass_weight = 0

    while len(visited) < num_of_nodes - 1:
        minimum = 99999
        best_visit = 100000
        for node in visited:
            for unv_node in unvisited:
                for element in data:
                    if node in element and unv_node in element and minimum > int(element[2]["weight"]):
                        minimum = element[2]["weight"]
                        best_visit = unv_node
        carcass_weight += minimum
        unvisited.remove(best_visit)
        visited.append(best_visit)
    return carcass_weight



    # print(graph.nodes)
    # print(in_set)
    # #for edge in data:
     #   pass



if __name__ == "__main__":
    graph = gnp_random_connected_graph(10, 1, False)
    print(graph.edges.data())
    print(prims_algo(graph))


