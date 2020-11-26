import bct
from reports import plots
import matplotlib.pyplot as plt


class DegreeCorrelation:
    def __init__(self, graphA, graphB, nameA, nameB):
        self.gA = graphA
        self.gB = graphB
        self.nameA = nameA
        self.nameB = nameB

    # returns a nparray with the sum of weights of each node
    def compute(self):
        centrality_A = bct.degrees_und(self.gA)
        centrality_B = bct.degrees_und(self.gB)

        plots.create_plot("reports/plots/" + self.nameA + '_' + self.nameB + "_degree_correlation.pdf",
                          self.nameA + " Degree vs. " + self.nameB + " Degree",
                          self.nameA + " Degree", centrality_A,
                          self.nameB + " Degree", centrality_B,
                          also_log_scale=False, yticks=[0, 45])

        plt.show()

        return


