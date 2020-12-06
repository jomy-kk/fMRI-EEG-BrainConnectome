import BrainConnectivityToolboxWrapper as b
import pandas as pd
import datetime
from matplotlib import pyplot as plt
from DesikanViz import write_desikan

most_recent_stats = None


def analyze(graph, graph_binarized, name, show=False,
            degree_centrality=True,
            node_strength=True,
            clustering_coeff=True,
            weighted_clustering_coeff=True,
            average_path_len=True,
            betweenness_centrality=True,
            rich_club=True,
            newman_modularity=True,
            edge_betweenness=True,
            participation_coefficient=True,
            communities_algorithm='all',
            desikan_metric=None,
            lobe=None):


    # Force dependent measures
    if edge_betweenness:
        rich_club = True

    if rich_club:
        #degree centrality is needed for the rich club
        degree_centrality = True


    # Select submatrix

    #LEFT
    #graph = graph[:34, :34]

    #RIGHT
    #graph = graph[34:, 34:]

    #INTER HLHR
    #graph = graph[34:, :34]


    # Analyze

    nodes = [i for i in range(len(graph[0]))]

    stats = pd.DataFrame(nodes)
    stats.columns = ['Node']

    if degree_centrality:
        stats = b.DegreeCentrality(graph, name, stats).compute()

    if node_strength:
        stats = b.NodeStrength(graph, name, stats, show).compute()

    if clustering_coeff:
        stats = b.ClusteringCoefficient(graph, name, stats).compute()

    if weighted_clustering_coeff:
        stats = b.WeightedClusteringCoefficient(graph, name, stats).compute()

    if average_path_len:
        b.AveragePathLength(graph, name, stats).compute()

    if betweenness_centrality:
        stats = b.BetweennessCentrality(graph, name, stats).compute()

    if rich_club:
        stats, rich = b.RichClubCoefficient(graph, name, stats).compute()

    if newman_modularity:
        b.NewmanModularity(graph_binarized, name, stats, communities_algorithm).compute()

    if edge_betweenness:
        b.EdgeBetweennessCentrality(graph, name, stats, rich).compute()

    if participation_coefficient:
        b.ParticipationCoefficient(graph, name, stats, communities_algorithm).compute()


    if desikan_metric:
        if desikan_metric not in stats:
            print("The specified metric must be the name of a column of the stats file")

        write_desikan(desikan_metric, name, stats[desikan_metric].to_list())

    # Save stats

    global most_recent_stats
    most_recent_stats = stats

    stats.to_csv("stats/stats-" + name + "-" + str(datetime.datetime.now()).replace(':', '-'), sep=' ')


def plot_relation(xaxis_stats_label, yaxis_stats_label):
    global most_recent_stats

    plt.plot(most_recent_stats[xaxis_stats_label].to_list(), most_recent_stats[yaxis_stats_label].to_list())
    plt.xlabel(xaxis_stats_label)
    plt.ylabel(yaxis_stats_label)
    plt.show()
