import bct

import statistics


class BetweennessCentrality:
    def __init__(self, graph, name, stats):
        self.g = graph
        self.name = name
        self.stats = stats

    # returns a nparray with the degree of each node
    def compute(self):
        # binarize the matrix 1st and pass the binzared to the unweighed. otherwise, it'll all be 0s
        centrality_unweighted = bct.betweenness_bin(self.g)
        centrality_weighted = bct.betweenness_wei(self.g)
        self.stats['Betweenness Unweighted'] = [v for v in centrality_unweighted]
        self.stats['Betweenness Weighted'] = [v for v in centrality_weighted]

        return self.stats

