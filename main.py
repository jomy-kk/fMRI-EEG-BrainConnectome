import scipy.io as io
from BrainConnectivityToolboxWrapper.Analyser import analyze, plot_relation
from BrainConnectivityToolboxWrapper import DegreeCorrelation

##########################################
# Analyzing the 7 static weighted matrices
##########################################

input_file = "data/processed/matrices/static_adjacency_matrices.mat"
#names = ['fmri', 'broad', 'delta', 'theta', 'alpha', 'beta', 'gamma']

names = ['fmri']

matrixes = {name: io.loadmat(input_file).get(name) for name in names}

'''for n in matrixes:
    print("################")
    print("Analyzing: " + n)
    # For example, in this run we are computing all metrics but WCC, printing a desikan template file with node
    # strength as feature
    analyze(matrixes[n], n,
            degree_centrality=False,
            node_strength=False,
            clusering_coeff=False,
            weighted_clustering_coeff=False,
            average_path_len=False,
            betweenness_centrality=False,
            newman_modularity=False,
            edge_betweenness=True,
            rich_club=False)
'''
