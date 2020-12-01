import networkx as nx
import bct
import numpy as np
import itertools

class NewmanModularity:
    def __init__(self, graph, name, stats):
        self.g = graph
        self.name = name
        self.stats = stats

    def compute(self):

        ### Test
        #G = nx.from_numpy_matrix(self.g)
        #comp = self.get_communities_GM(G)
        #limited = itertools.takewhile(lambda c: len(c) <= 14, comp)
        #for communities in limited:
            #print(tuple(sorted(c) for c in communities))
        #modularity = nx.algorithms.community.quality.modularity(G, communities)

        communities = bct.community_louvain(self.g)
        print(communities)
        modularity = communities[1]
        n_communities = np.max(communities[0])
        print("\nCommunity Louvain Algorithm: ")
        print("#Communities: ", n_communities)
        print("Modularity: ", modularity)
        for i in range(n_communities):
            print("\nCommunity 1: ", [np.where(communities[0][k] == i, communities[0][k], None) for k in range(68)])











