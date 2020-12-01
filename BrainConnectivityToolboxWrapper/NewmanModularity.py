import networkx as nx
import bct
import numpy as np
import pandas as pd
from collections import OrderedDict
from cdlib import algorithms

class NewmanModularity:
    def __init__(self, graph, name, stats):
        self.g = graph
        self.name = name
        self.stats = stats

    def compute(self):

        template = pd.read_csv("data/lobes.node", " ", header='infer')

        G = nx.Graph(self.g)
        result = algorithms.louvain(G)
        modularity = result.newman_girvan_modularity().score
        significance = result.significance().score
        communities = result.to_node_community_map()
        n_communities = list(communities.values())[-1][0] + 1
        print("\nLouvain Algorithm: ")
        print("#Communities: ", n_communities)
        print("Modularity: ", modularity)
        print("Significance: ", significance)
        template['Louvain'] = get_ordered_communities(communities)
        print("\n")

        G = nx.Graph(self.g)
        result = algorithms.infomap(G)
        modularity = result.newman_girvan_modularity().score
        significance = result.significance().score
        communities = result.to_node_community_map()
        n_communities = list(communities.values())[-1][0] + 1
        print("\nInfomap Algorithm: ")
        print("#Communities: ", n_communities)
        print("Modularity: ", modularity)
        print("Significance: ", significance)
        template['Infomap'] = get_ordered_communities(communities)
        print("\n")

        G = nx.Graph(self.g)
        result = algorithms.spinglass(G)
        modularity = result.newman_girvan_modularity().score
        significance = result.significance().score
        communities = result.to_node_community_map()
        n_communities = list(communities.values())[-1][0] + 1
        print("\nSpinglass Algorithm: ")
        print("#Communities: ", n_communities)
        print("Modularity: ", modularity)
        print("Significance: ", significance)
        template['Spinglass'] = get_ordered_communities(communities)
        print("\n")

        G = nx.Graph(self.g)
        result = algorithms.walktrap(G)
        modularity = result.newman_girvan_modularity().score
        significance = result.significance().score
        communities = result.to_node_community_map()
        n_communities = list(communities.values())[-1][0] + 1
        print("\nWalktrap Algorithm: ")
        print("#Communities: ", n_communities)
        print("Modularity: ", modularity)
        print("Significance: ", significance)
        template['Walktrap'] = get_ordered_communities(communities)
        print("\n")

        G = nx.Graph(self.g)
        result = algorithms.girvan_newman(G, level=3)
        modularity = result.newman_girvan_modularity().score
        significance = result.significance().score
        communities = result.to_node_community_map()
        n_communities = list(communities.values())[-1][0] + 1
        print("\nGirvan Newman: ")
        print("#Communities: ", n_communities)
        print("Modularity: ", modularity)
        print("Significance: ", significance)
        template['Girvan-Newman'] = get_ordered_communities(communities)
        print("\n")

        pd.DataFrame.to_csv(template, "Results/Communities/communities.csv", " ")



def get_ordered_communities(communities_dict):
    lst = list((OrderedDict(sorted(communities_dict.items()))).values())
    res = []
    for i in lst:
        res.append(i[0])
    return res

