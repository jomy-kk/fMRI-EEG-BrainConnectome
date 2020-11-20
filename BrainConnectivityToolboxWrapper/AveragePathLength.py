import bct
import scipy.io as io


class AveragePathLength:
    def __init__(self, graph, name, stats):
        self.g = graph
        self.name = name
        self.stats = stats
        self.binarized = io.loadmat("data/processed/matrices/static_unweighted_adjacency_matrices.mat").get(name)

    # returns a nparray with the sum of weights of each node
    # binarized only
    def compute(self):
        distance_matrix = bct.breadthdist(self.binarized)[1]
        metrics = bct.charpath(distance_matrix)

        print("Average Path Length: " + str(metrics[0]))
        print("Network Diameter: " + str(metrics[4]))

