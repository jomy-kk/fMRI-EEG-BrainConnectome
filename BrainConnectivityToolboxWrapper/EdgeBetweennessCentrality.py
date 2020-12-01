import bct
from reports import plots
import matplotlib.pyplot as plt
import statistics
import networkx as nx
import pandas as pd
from reports import plots


class EdgeBetweennessCentrality:
    def __init__(self, graph, name, stats, rich):
        self.g = graph
        self.name = name
        self.stats = stats
        self.rich = rich

    def compute(self):
        G = nx.from_numpy_matrix(self.g)

        weighted_edge_betweenness = nx.edge_betweenness_centrality(G, weight='weight')
        unweighted_edge_betweenness = nx.edge_betweenness_centrality(G)
        edges = list(G.edges)

        edge_stats = pd.DataFrame(edges)
        edge_stats.columns = ['Edge1', 'Edge2']

        edge_stats['W_EdgeBetweenness'] = edge_stats.apply(lambda row: weighted_edge_betweenness[(row.Edge1, row.Edge2)], axis=1)
        edge_stats['U_EdgeBetweenness'] = edge_stats.apply(lambda row: unweighted_edge_betweenness[(row.Edge1, row.Edge2)], axis=1)

        edge_stats['EdgeType'] = edge_stats.apply(lambda row: get_edge_type(row.Edge1, row.Edge2, self.rich, self.stats['Degree'].to_list()), axis=1)

        edge_stats.to_csv("stats/EDGE-stats-fmri", sep='\t')

        plots.create_box_plot('U_EdgeBetweenness')


def get_edge_type(x, y, rich, degree):
    if degree[int(x)] in rich or degree[int(y)] in rich:
        if degree[int(x)] in rich and degree[int(y)] in rich:
            return "rich"
        else:
            return "feeder"
    else:
        return "periphery"


