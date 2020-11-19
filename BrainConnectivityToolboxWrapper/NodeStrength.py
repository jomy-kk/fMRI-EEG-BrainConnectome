import bct
import statistics


class NodeStrength:
    def __init__(self, graph, name, stats):
        self.g = graph
        self.name = name
        self.stats = stats

    # returns a nparray with the sum of weights of each node
    def compute(self):
        weights = bct.strengths_und(self.g)
        self.stats['Strength'] = [v for v in weights]
        average = statistics.mean(self.stats['Strength'])
        print("Average Strength: " + str(average) + "\n")
        return self.stats


