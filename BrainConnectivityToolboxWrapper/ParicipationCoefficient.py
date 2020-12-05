import bct
from reports import plots
import matplotlib.pyplot as plt
import statistics
import cdlib
import networkx as nx
import pandas as pd
from reports import plots
from BrainConnectivityToolboxWrapper import NewmanModularity as NM


class ParticipationCoefficient:
    def __init__(self, graph, name, stats, communities_algorithm):
        self.g = graph
        self.name = name
        self.stats = stats
        self.communities_algorithm = communities_algorithm

    def compute(self):
        communities = NM(self.g, self.name, self.stats, self.communities_algorithm).compute()
        print(communities)
        participations = bct.participation_coef(self.g, communities, 'undirected')
        print('Participations', participations)
        within_degrees = bct.module_degree_zscore(self.g, communities, 0)
        print('Within Degrees Z-score', within_degrees)

        plots.create_plot_communitycolored("reports/plots/ParticipationCoeff/" + str(self.name) + '_' + str(self.communities_algorithm) + ".pdf",
                                           'title', 'Within-module Degree Z-score', within_degrees,
                                           'Participation Coefficient', participations,
                                           communities=communities)


def get_edge_type(x, y, rich, degree):
    if degree[int(x)] in rich or degree[int(y)] in rich:
        if degree[int(x)] in rich and degree[int(y)] in rich:
            return "rich"
        else:
            return "feeder"
    else:
        return "periphery"


