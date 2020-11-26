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

        print("Community Louvain Algorithm: ")
        print("#Communities: ", len(np.unique(communities[0])))
        print("Modularity: ", modularity)










