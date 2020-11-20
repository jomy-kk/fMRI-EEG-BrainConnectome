import bct
import scipy.io as io


class BetweennessCentrality:
    def __init__(self, graph, name, stats):
        self.g = graph
        self.name = name
        self.stats = stats
        self.binarized = io.loadmat("data/processed/matrices/static_unweighted_adjacency_matrices.mat").get(name)

    # returns a nparray with the degree of each node
    def compute(self):
        centrality_unweighted = bct.betweenness_bin(self.binarized)
        centrality_weighted = bct.betweenness_wei(self.g)
        self.stats['Betweenness Unweighted'] = [v for v in centrality_unweighted]
        self.stats['Betweenness Weighted'] = [v for v in centrality_weighted]

        return self.stats

