import bct
from reports import plots
import matplotlib.pyplot as plt
import statistics


class DegreeCentrality:
    def __init__(self, graph, name, stats):
        self.g = graph
        self.name = name
        self.stats = stats

    # returns a nparray with the degree of each node
    def compute(self):
        centrality = bct.degrees_und(self.g)

        self.stats['Degree'] = [v for v in centrality]

        # Degree distribution
        distribution = self.stats.groupby(['Degree']).size().reset_index(name='Frequency')
        sum = distribution['Frequency'].sum()
        distribution['Probability'] = distribution['Frequency'] / sum
        distribution.head(10)

        alpha = plots.create_plot("reports/plots/" + self.name + "_degree_distribution.pdf", 'Degree' + " distribution",
                                  'Degree', distribution['Degree'],
                                  "Probability", distribution['Probability'],
                                  yticks=[0, 1],
                                  also_log_scale=True, log_yticks=[11e-3, 1e-2, 1],
                                  powerlaw_xmin=1e1, powerlaw_xmax=1e4, xforplaw=self.stats["Degree"].to_list())

        plt.show()

        average = statistics.mean(self.stats['Degree'])

        print('Degree distribution gamma= ' + str(alpha) + "\n")

        print("Average Degree = " + str(average) + "\n")

        return self.stats
