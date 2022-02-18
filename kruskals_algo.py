"""
Kruskal's algorithm here.
"""
import networkx as nx
import matplotlib.pyplot as plt

from main import gnp_random_connected_graph

def kruskalls_tree(G: nx.Graph) -> nx.Graph:
    nodes_set = set()
    weight = 0
    spanning = nx.Graph()

    for node in G.nodes:
        nodes_set.add(frozenset([node]))

    for edge in sorted(list(G.edges(data=True)), key=lambda x: x[2]['weight']):
        if len(spanning.edges()) == len(G.nodes) - 1:
            print('spanning tree is done!')
            break
        for u_node_group in nodes_set:
            if edge[0] in u_node_group:
                if edge[1] in u_node_group:
                    break
                else:
                    for v_node_group in nodes_set:
                        if edge[1] in v_node_group:
                            spanning.add_edge(edge[0], edge[1], **edge[2])
                            weight += edge[2]['weight']
                            nodes_set -= {u_node_group, v_node_group}
                            nodes_set.add(frozenset(u_node_group | v_node_group))
                            # print(f'{edge} is to be added to spanning tree')
                            # print(nodes_set)
                            break
                    break
    return spanning, weight


if __name__ == '__main__':
    my_g = gnp_random_connected_graph(10, 1, True)
    print(*kruskalls_tree(my_g))
    plt.show()