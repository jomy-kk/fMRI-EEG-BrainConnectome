import networkx as nx
import bct
import numpy as np
import pandas as pd
from collections import OrderedDict
from cdlib import algorithms
from reports.plots import create_communities_table
import os.path
import BrainConnectivityToolboxWrapper.DegreeCentrality as DC

class NewmanModularity:
    def __init__(self, graph, name, stats):
        self.g = graph
        self.name = name
        self.stats = stats

    def compute(self):
        names = ["Louvain", "Infomap", "Spinglass", "Walktrap", "Girvan-Newman"]
        centrality = bct.degrees_und(self.g)
        region_names = pd.read_csv("data/lobes.node", " ", header='infer')['RegionName']

        template = pd.read_csv("data/communities_template.node", " ", header='infer')
        saveTo = "Results/Communities/" + self.name + "_louvian_communities.node"
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
        a = get_ordered_communities(communities)
        template['Louvain'] = a
        print("\n")
        template['Degree'] = [v for v in centrality]
        template['RegionName'] = region_names
        pd.DataFrame.to_csv(template, saveTo, " ", header=False, index=False)

        template = pd.read_csv("data/communities_template.node", " ", header='infer')
        saveTo = "Results/Communities/" + self.name + "_infomap_communities.node"
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
        b = get_ordered_communities(communities)
        template['Infomap'] = b
        print("\n")
        template['Degree'] = [v for v in centrality]
        template['RegionName'] = region_names
        pd.DataFrame.to_csv(template, saveTo, " ", header=False, index=False)

        template = pd.read_csv("data/communities_template.node", " ", header='infer')
        saveTo = "Results/Communities/" + self.name + "_spinglass_communities.node"
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
        c = get_ordered_communities(communities)
        template['Spinglass'] = c
        print("\n")
        template['Degree'] = [v for v in centrality]
        template['RegionName'] = region_names
        pd.DataFrame.to_csv(template, saveTo, " ", header=False, index=False)

        template = pd.read_csv("data/communities_template.node", " ", header='infer')
        saveTo = "Results/Communities/" + self.name + "_walktrap_communities.node"
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
        d = get_ordered_communities(communities)
        template['Walktrap'] = d
        print("\n")
        template['Degree'] = [v for v in centrality]
        template['RegionName'] = region_names
        pd.DataFrame.to_csv(template, saveTo, " ", header=False, index=False)

        template = pd.read_csv("data/communities_template.node", " ", header='infer')
        saveTo = "Results/Communities/" + self.name + "_girvannewman_communities.node"
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
        e = get_ordered_communities(communities)
        template['Girvan-Newman'] = e
        print("\n")
        template['Degree'] = [v for v in centrality]
        template['RegionName'] = region_names
        pd.DataFrame.to_csv(template, saveTo, " ", header=False, index=False)




def get_ordered_communities(communities_dict):
    lst = list((OrderedDict(sorted(communities_dict.items()))).values())
    res = []
    for i in lst:
        res.append(i[0])
    return np.array(res)

