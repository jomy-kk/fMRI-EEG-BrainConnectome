import bct
import statistics


class ClusteringCoefficient:
    def __init__(self, graph, name, stats):
        self.g = graph
        self.name = name
        self.stats = stats

    # returns a nparray with the sum of weights of each node
    def compute(self):
        # supposed to be the binarized matrix
        cc = bct.clustering_coef_bu(self.g)

        self.stats['CluseringCoefficient'] = [v for v in cc]
        average = statistics.mean(self.stats['CluseringCoefficient'])

        print("Average Clustering Coefficient: " + str(average) + "\n")
        return self.stats
