import bct
import statistics


class WeightedClusteringCoefficient:
    def __init__(self, graph, name, stats):
        self.g = graph
        self.name = name
        self.stats = stats

    # returns a nparray with the sum of weights of each node
    def compute(self):
        # supposed to be the binarized matrix
        wcc = bct.clustering_coef_wu(self.g)

        self.stats['WeightedCluseringCoefficient'] = [v for v in wcc]
        average = statistics.mean(self.stats['WeightedCluseringCoefficient'])

        print("Average Weighted Clustering Coefficient: " + str(average) + "\n")
        return self.stats
