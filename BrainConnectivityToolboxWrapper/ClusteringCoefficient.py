import bct
import statistics
import scipy.io as io


class ClusteringCoefficient:
    def __init__(self, graph, name, stats):
        self.g = graph
        self.name = name
        self.stats = stats
        self.binarized = io.loadmat("data/processed/matrices/static_unweighted_adjacency_matrices.mat").get(name)

    # returns a nparray with the sum of weights of each node
    # binarized only
    def compute(self):
        cc = bct.clustering_coef_bu(self.binarized)

        self.stats['CluseringCoefficient'] = [v for v in cc]
        average = statistics.mean(self.stats['CluseringCoefficient'])

        print("Average Clustering Coefficient: " + str(average) + "\n")
        return self.stats
