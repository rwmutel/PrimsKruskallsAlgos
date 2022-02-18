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
    time_taken_prim = 0
    time_taken_kruskal = 0
    ITERATIONS = 100
    for i in tqdm(range(ITERATIONS)):
        G = gnp_random_connected_graph(20, 1, False)

        start = time.time()
        prims_algo(G)
        end = time.time()
        time_taken_prim += end - start

        start = time.time()
        kruskalls_tree(G)
        end = time.time()
        time_taken_kruskal += end - start

    
    print('Prim:')
    print(time_taken_prim / ITERATIONS)
    print('\nKruskal:')
    print(time_taken_kruskal / ITERATIONS)