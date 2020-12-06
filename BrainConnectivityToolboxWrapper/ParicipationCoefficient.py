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
        try:
            name = "Results/Communities/" + self.name + "_" + self.communities_algorithm + "_communities.node"
            print('Trying', name)
            last_results = pd.read_csv(name, " ", names=['X','Y','Z','Community', 'Degree', 'RegionName'])
            print('Loading communities...')
            communities = last_results['Community']
            region_names = last_results['RegionName']

        except Exception:
            print('Divinding communities...')
            communities = NM(self.g, self.name, self.stats, self.communities_algorithm).compute()
            region_names = pd.read_csv("data/lobes.node", " ", header='infer')['RegionName']

        participations = bct.participation_coef(self.g, communities, 'undirected')
        within_degrees = bct.module_degree_zscore(self.g, communities, 0)

        connectors, provincials = [], []
        for node in zip(participations, within_degrees, region_names):
            if node[1] > 1:
                if node[0] > 0.6:
                    connectors.append((node[2], node[1], node[0]))
                if node[0] < 0.4:
                    provincials.append((node[2], node[1], node[0]))

        print("Connectors", connectors)
        print("Provincials", provincials)

        self.stats['RegionName'] = region_names
        self.stats['Community'] = communities
        self.stats['wMD'] = within_degrees
        self.stats['PC'] = participations


        plots.create_plot_communitycolored("reports/plots/ParticipationCoeff/" + str(self.name) + '_' + str(self.communities_algorithm) + ".pdf",
                                           ('fMRI' if self.name=='fmri' else 'EEG-'+self.name),
                                           'Within-module Degree Z-score', within_degrees,
                                           'Participation Coefficient', participations,
                                           communities=communities, xticks=[-3,-2,-1,0,1,2,3], yticks=[0,0.2,0.4,0.6,0.8,1.0])


        return self.stats

def get_edge_type(x, y, rich, degree):
    if degree[int(x)] in rich or degree[int(y)] in rich:
        if degree[int(x)] in rich and degree[int(y)] in rich:
            return "rich"
        else:
            return "feeder"
    else:
        return "periphery"


