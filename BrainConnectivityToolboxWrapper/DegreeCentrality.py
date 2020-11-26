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

        # Lobe grouping
        plots.create_bar_lobe_grouped_descending("reports/plots/" + self.name + "_degree_descending.pdf", self.name + " Degree Centrality",
                                 'Degree', centrality)

        plt.show()
        '''
        # Degree distribution
        distribution = self.stats.groupby(['Degree']).size().reset_index(name='Frequency')
        sum = distribution['Frequency'].sum()
        distribution['Probability'] = distribution['Frequency'] / sum
        distribution.head(10)

        alpha = plots.create_bar("reports/plots/" + self.name + "_degree_distribution.pdf", self.name + " Degree Distribution",
                                 'Degree', distribution['Degree'],
                                 'Probability', distribution['Probability'],
                                  yticks=[0, 0.05, 0.1, 0.15])

        plt.show()
        '''
        average = statistics.mean(self.stats['Degree'])

        #print('Degree distribution gamma= ' + str(alpha) + "\n")

        print("Average Degree = " + str(average) + "\n")

        return self.stats
