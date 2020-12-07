import scipy.io as io
from BrainConnectivityToolboxWrapper.Analyser import analyze, plot_relation
from BrainConnectivityToolboxWrapper import DegreeCorrelation
import networkx as nx
import numpy as np
import BrainConnectivityToolboxWrapper as b
from matplotlib import pyplot as plt

##########################################
# Analyzing the 7 static weighted matrices
##########################################

names = ['fmri', 'broad', 'delta', 'theta', 'alpha', 'beta', 'gamma']
names = ['alpha']
input_file = "data/processed/matrices/static_adjacency_matrices.mat"
input_file_binarized = "data/processed/matrices/static_unweighted_adjacency_matrices.mat"

matrixes = {name: io.loadmat(input_file).get(name) for name in names}
matrixes_binarized = {name: io.loadmat(input_file).get(name) for name in names}

for n in matrixes:
    print("################")
    print("Analyzing: " + n)
    # For example, in this run we are computing all metrics but WCC, printing a desikan template file with node
    # strength as feature
    analyze(matrixes[n], matrixes_binarized[n], n,
            degree_centrality=False,
            node_strength=False,
            clustering_coeff=False,
            weighted_clustering_coeff=False,
            average_path_len=False,
            betweenness_centrality=False,
            newman_modularity=False,
            edge_betweenness=False,
            rich_club=True,
            participation_coefficient=False,
            communities_algorithm='louvain',
            desikan_metric='RichClubDegCoeff'
            )

'''for n in matrixes:
    print(n)
    network = nx.Graph(matrixes[n])
    random_network = nx.gnm_random_graph(network.number_of_nodes(), network.number_of_edges())
    print("<C> =", nx.average_clustering(random_network))
    print("APL =", nx.average_shortest_path_length(random_network))
    print("d =", nx.diameter(random_network))
    print("D =", 2*network.number_of_edges()/(network.number_of_nodes()*(network.number_of_nodes()-1)))
    #print(nx.density(network))
    print()
'''

'''
left_intra_table, right_intra_table, left_inter_table, right_inter_table, left_right_intra_table, left_right_inter_table = [], [], [], [], [], []
for lobe in range(1,8):
    left_intra_row, right_intra_row, left_inter_row, right_inter_row, left_right_intra_row, left_right_inter_row = [], [], [], [], [], []
    for n in matrixes:
        left_intra_average, right_intra_average, left_inter_average, right_inter_average, left_right_intra_average, left_right_inter_average = b.DegreeCentrality(matrixes[n], n, None, lobe=lobe).compute()
        left_intra_row.append(left_intra_average)
        right_intra_row.append(right_intra_average)
        left_inter_row.append(left_inter_average)
        right_inter_row.append(right_inter_average)
        left_right_intra_row.append(left_right_intra_average)
        left_right_inter_row.append(left_right_inter_average)

    left_intra_table.append(left_intra_row)
    right_intra_table.append(right_intra_row)
    left_inter_table.append(left_inter_row)
    right_inter_table.append(right_inter_row)
    left_right_intra_table.append(left_right_intra_row)
    left_right_inter_table.append(left_right_inter_row)

tables = [np.array(left_intra_table), np.array(right_intra_table), np.array(left_inter_table),
          np.array(right_inter_table), np.array(left_right_intra_table), np.array(left_right_inter_table)]

titles = ["Intra-Lobe Average Degree (left hemisphere)",
          "Intra-Lobe Average Degree (right hemisphere)",
          "Inter-Lobe Average Degree (left hemisphere)",
          "Inter-Lobe Average Degree (right hemisphere)",
          "Corresponding-Lobe Average Degree (both hemispheres)",
          "Inter-Lobe Average Degree (both hemispheres)",
          ]

rows = ["Temporal (medial)", "Temporal (lateral)", "Frontal", "Parietal", "Occipital", "Cingulate", "Insula"]
columns = ["fMRI", "EEG-broad", "EEG-delta", "EEG-theta", "EEG-alpha", "EEG-beta", "EEG-gamma"]

for i in range(len(tables)):
    #ax = plt.subplot()
    #ax.axis('off')
    #ax.axis('tight')
    fig = plt.figure(figsize=(5, 2))
    plt.axis('off')

    cols_fmri = tables[i][:,0:1]
    cols_eeg = tables[i][:,1:]


    norm_fmri = plt.Normalize(cols_fmri.min() - 1, cols_fmri.max() + 1)
    norm_eeg = plt.Normalize(cols_eeg.min() - 1, cols_eeg.max() + 1)
    colors_fmri = plt.cm.Wistia(norm_fmri(cols_fmri))
    colors_eeg = plt.cm.cool(norm_eeg(cols_eeg))

    colors = np.concatenate([colors_fmri,colors_eeg], 1)

    plt.table([['%.2f' % j for j in i] for i in tables[i]], rowLabels=rows, colLabels=columns, loc='center',
                      cellColours=colors, colWidths=[0.1]*7)

    plt.title(titles[i], fontsize=8)
    #fig.colorbar(plt.cm.ScalarMappable(norm=norm_fmri, cmap='Wistia'))
    #fig.colorbar(plt.cm.ScalarMappable(norm=norm_eeg, cmap='cool'))

    plt.show()
    fig.savefig("reports/tables/"+ titles[i] +"_avg_degree.pdf", bbox_inches = 'tight', pad_inches = 0)

'''
