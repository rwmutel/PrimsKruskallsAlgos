import random
import networkx as nx
from tqdm import tqdm
import time
import matplotlib.pyplot as plt
from itertools import combinations, groupby
from prims_algo import prims_algo
from kruskals_algo import kruskalls_tree

'''
Discrete math laboratory work #01
Done by Roman Mutel and Marko Ruzak
'''

def gnp_random_connected_graph(num_of_nodes: int,
                               completeness: int,
                               draw: bool = False) -> 'list[tuple[int, int]]':
    """
    Generates a random undirected graph, similarly to an Erdős-Rényi 
    graph, but enforcing that the resulting graph is conneted.

    Source: 'GraphGeneration.ipynb'
    """

    edges = combinations(range(num_of_nodes), 2)
    G = nx.Graph()
    G.add_nodes_from(range(num_of_nodes))
    
    for _, node_edges in groupby(edges, key = lambda x: x[0]):
        node_edges = list(node_edges)
        random_edge = random.choice(node_edges)
        G.add_edge(*random_edge)
        for e in node_edges:
            if random.random() < completeness:
                G.add_edge(*e)
                
    for (u,v,w) in G.edges(data=True):
        w['weight'] = random.randint(0,10)
                
    if draw: 
        plt.figure(figsize=(10,6))
        nx.draw(G, node_color='lightblue', 
            with_labels=True, 
            node_size=500)
    
    return G

if __name__ == '__main__':
    time_nx_prim = 0
    y_nx_prim = []
    time_prim = 0
    y_prim = []
    time_nx_kruskal = 0
    y_nx_kruskal = []
    time_kruskal = 0
    y_kruskal = []
    ITERATIONS = 10
    nodes = [50 * i for i in range(15)]
    fig, ax = plt.subplots()

    for n in nodes:
        for i in tqdm(range(ITERATIONS)):
            G = gnp_random_connected_graph(n, 1, False)

            start = time.time()
            nx.minimum_spanning_tree(G, algorithm='prim')
            end = time.time()
            time_nx_prim += end - start

            start = time.time()
            # prims_algo(G)
            end = time.time()
            time_prim += end - start

            start = time.time()
            nx.minimum_spanning_tree(G, algorithm='kruskal')
            end = time.time()
            time_nx_kruskal += end - start

            start = time.time()
            kruskalls_tree(G)
            end = time.time()
            time_kruskal += end - start
        
        y_nx_prim.append(time_nx_prim/ITERATIONS)
        y_prim.append(time_prim/ITERATIONS)
        y_nx_kruskal.append(time_nx_kruskal/ITERATIONS)
        y_kruskal.append(time_kruskal/ITERATIONS)

    ax.plot(nodes, y_nx_prim, label='NetworkX Prim')
    ax.plot(nodes, y_prim, label='Our Prim')
    ax.plot(nodes, y_nx_kruskal, label='NetworkX Kruskal')
    ax.plot(nodes, y_kruskal, label='Our Kruskal')
    ax.legend()
    plt.title('Comparison of Different Minimum Spanning Tree Algorithms')
    plt.xlabel('Amount of nodes in a complete graph')
    plt.ylabel('Time (seconds)')
    plt.show()