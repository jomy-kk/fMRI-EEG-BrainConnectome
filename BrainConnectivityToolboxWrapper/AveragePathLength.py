import bct
import statistics


class AveragePathLength:
    def __init__(self, graph, name, stats):
        self.g = graph
        self.name = name
        self.stats = stats

    # returns a nparray with the sum of weights of each node
    def compute(self):
        distance_matrix = bct.breadthdist(self.g)[1]
        metrics = bct.charpath(distance_matrix)

        print("Average Path Length: " + str(metrics[0]))
        print("Network Diameter: " + str(metrics[4]))

