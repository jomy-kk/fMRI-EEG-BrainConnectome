import bct
import networkx as nx
import pandas as pd
from reports import plots
import scipy.io as io


class EdgeBetweennessCentrality:
    def __init__(self, graph, name, stats, rich):
        self.g = graph
        self.name = name
        self.stats = stats
        self.rich = rich
        self.binarized = io.loadmat("data/processed/matrices/static_unweighted_adjacency_matrices.mat").get(name)

    def compute(self):
        G = nx.from_numpy_matrix(self.g)

        edges = list(G.edges)
        counter = {'rich': 0, 'feeder': 0, 'periphery': 0}

        for i in range(len(self.g)):
            for j in range(len(self.g[i])):
                if self.g[i][j] != 0:
                    self.g[i][j] = 1/self.g[i][j]

        weighted_edge_betweenness = bct.edge_betweenness_wei(self.g)
        unweighted_edge_betweenness = bct.edge_betweenness_bin(self.binarized)

        print("###########################")
        print(unweighted_edge_betweenness)

        edge_stats = pd.DataFrame(edges)
        edge_stats.columns = ['Edge1', 'Edge2']

        print(edge_stats.head())

        edge_stats['W_EdgeBetweenness'] = edge_stats.apply(
            lambda row: weighted_edge_betweenness[0][row.Edge1][row.Edge2], axis=1)

        print(edge_stats.head())

        edge_stats['U_EdgeBetweenness'] = edge_stats.apply(
            lambda row: unweighted_edge_betweenness[0][int(row.Edge1)][int(row.Edge2)], axis=1)

        print(edge_stats.head())

        edge_stats['EdgeType'] = edge_stats.apply(
            lambda row: get_edge_type(row.Edge1, row.Edge2, self.rich, self.stats['Degree'].to_list(), counter), axis=1)

        print("Number of edge per type: ")
        print(counter)

        edge_stats.to_csv("stats/EDGE-stats-fmri", sep='\t')

        plots.create_box_plot_edges('W_EdgeBetweenness')


def get_edge_type(x, y, rich, degree, counter):
    if degree[int(x)] in rich or degree[int(y)] in rich:
        if degree[int(x)] in rich and degree[int(y)] in rich:
            counter['rich'] += 1
            return "rich"
        else:
            counter['feeder'] += 1
            return "feeder"
    else:
        counter['periphery'] += 1
        return "periphery"
