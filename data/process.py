import scipy.io as io
import numpy as np
import networkx as nx
import bct
from reports import plots

# load pre-processed
fMRI_path = "pre-processed/conn_desi_phase_coh_time_fmri.mat"
broad_EEG_path = "pre-processed/conn_desi_cohi_time_eeg_broad_correct_subj1-7T_.mat"
delta_EEG_path = "pre-processed/conn_desi_cohi_time_eeg_delta_correct_subj1-7T_.mat"
theta_EEG_path = "pre-processed/conn_desi_cohi_time_eeg_theta_correct_subj1-7T_.mat"
alpha_EEG_path = "pre-processed/conn_desi_cohi_time_eeg_alpha_correct_subj1-7T.mat"
beta_EEG_path = "pre-processed/conn_desi_cohi_time_eeg_beta_correct_subj1-7T_.mat"
gamma_EEG_path = "pre-processed/conn_desi_cohi_time_eeg_gamma_correct_subj1-7T_.mat"

# create arrays and synchronize EEG with fMRI (fMRI is delayed 3 seconds)
fMRI = np.delete((io.loadmat(fMRI_path)).get('connFMRI'), np.s_[0:3], 2)
broad_EEG = np.delete((io.loadmat(broad_EEG_path)).get('connEEGbroad'), np.s_[:3], 2)
delta_EEG = np.delete((io.loadmat(delta_EEG_path)).get('connEEGdelta'), np.s_[:3], 2)
theta_EEG = np.delete((io.loadmat(theta_EEG_path)).get('connEEGtheta'), np.s_[:3], 2)
alpha_EEG = np.delete((io.loadmat(alpha_EEG_path)).get('connEEGalpha'), np.s_[:3], 2)
beta_EEG = np.delete((io.loadmat(beta_EEG_path)).get('connEEGbeta'), np.s_[:3], 2)
gamma_EEG = np.delete((io.loadmat(gamma_EEG_path)).get('connEEGgamma'), np.s_[:3], 2)

# create static arrays (no time series)
static_fMRI = np.average(fMRI, 2)
static_broad_EEG = np.average(broad_EEG, 2)
static_delta_EEG = np.average(delta_EEG, 2)
static_theta_EEG = np.average(theta_EEG, 2)
static_alpha_EEG = np.average(alpha_EEG, 2)
static_beta_EEG = np.average(beta_EEG, 2)
static_gamma_EEG = np.average(gamma_EEG, 2)


# threshold fMRI
#plots.plot_connectivity_matrix(static_fMRI, "Connectivity", "No threshold", "static_fMRI", False)
bct.threshold_absolute(static_fMRI, thr=0, copy=False)
#plots.plot_connectivity_matrix_thresholded(static_fMRI, "Connectivity", "Threshold > 0", "static_fMRI_threshold0", False)
static_fMRI_unweighted = bct.weight_conversion(static_fMRI, 'binarize', copy=True)
#plots.plot_connectivity_matrix_binarized(static_fMRI_unweighted, "Unweighted (binarized)", "static_fMRI_unweighted", False)

# threshold EEGs
names = ("static_broad_EEG", "static_delta_EEG", "static_theta_EEG", "static_alpha_EEG", "static_beta_EEG", "static_gamma_EEG")
matrices = [static_broad_EEG, static_delta_EEG, static_theta_EEG, static_alpha_EEG, static_beta_EEG, static_gamma_EEG]
matrices_unweighted = []

for i in range(len(names)):
    #plots.plot_connectivity_matrix(matrices[i], "Connectivity", "No threshold", names[i], False)
    mean = np.mean(matrices[i])
    bct.threshold_absolute(matrices[i], thr=0.05, copy=False)
    #plots.plot_connectivity_matrix_thresholded(matrices[i], "Connectivity", "Threshold > " + ('%.4f' % mean), names[i] + "_threshold_" + ('%.4f' % mean), False)
    unweighted = bct.weight_conversion(matrices[i], 'binarize', copy=True)
    matrices_unweighted.append(unweighted)
    #plots.plot_connectivity_matrix_binarized(unweighted, "Unweighted (binarized)", names[i] + "_unweighted", False)


dtype = [("fmri", float), ("broad", float), ("delta", float), ("theta", float), ("alpha", float), ("beta", float), ("gamma", float)]
matrices.insert(0, static_fMRI)
matrices_unweighted.insert(0, static_fMRI_unweighted)

# save adjacency matrices
mat_file = {}
for i in range(len(matrices)):
    mat_file[dtype[i]] = matrices[i]
io.savemat("processed/static_adjacency_matrices.mat", mat_file)
mat_file = {}
for i in range(len(matrices_unweighted)):
    mat_file[dtype[i]] = matrices_unweighted[i]
io.savemat("processed/static_unweighted_adjacency_matrices.mat", mat_file)


# create static connectomes

# weighted
static_connectome = nx.Graph()
for i in range(len(static_fMRI)):
    for j in range(len(static_fMRI[0])):
        args = {'u_of_edge': i, 'v_of_edge': j}
        for attr in range(0, len(dtype)):
            weight = (matrices[attr])[i][j]
            if weight > 0:
                args[dtype[attr][0]] = weight
        if len(args) > 2:  # check if some weight was added
            static_connectome.add_edge(**args)

nx.write_edgelist(static_connectome, "processed/static_connectome.edges", data=True)

# unweighted
for attr in range(0, len(dtype)):
    static_connectome_unweighted = nx.Graph(matrices_unweighted[attr])
    nx.write_edgelist(static_connectome_unweighted, "processed/static_connectome_unweighted_"+ dtype[attr][0] +".edges", data=False)

exit(0)

