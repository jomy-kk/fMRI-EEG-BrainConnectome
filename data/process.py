import scipy.io as io
import numpy as np
import networkx as nx
import pickle as pk

# load pre-processed
fMRI_path = "data/pre-processed/conn_desi_phase_coh_time_fmri.mat"
broad_EEG_path = "data/pre-processed/conn_desi_cohi_time_eeg_broad_correct_subj1-7T_.mat"
delta_EEG_path = "data/pre-processed/conn_desi_cohi_time_eeg_delta_correct_subj1-7T_.mat"
theta_EEG_path = "data/pre-processed/conn_desi_cohi_time_eeg_theta_correct_subj1-7T_.mat"
alpha_EEG_path = "data/pre-processed/conn_desi_cohi_time_eeg_alpha_correct_subj1-7T.mat"
beta_EEG_path = "data/pre-processed/conn_desi_cohi_time_eeg_beta_correct_subj1-7T_.mat"
gamma_EEG_path = "data/pre-processed/conn_desi_cohi_time_eeg_gamma_correct_subj1-7T_.mat"

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

# apply a threshold
fmri_threshold = 0.3
eeg_threshold = 0.03
static_fMRI = (static_fMRI >= fmri_threshold) * static_fMRI
static_broad_EEG = (static_broad_EEG >= eeg_threshold) * static_broad_EEG
static_delta_EEG = (static_delta_EEG >= eeg_threshold) * static_delta_EEG
static_theta_EEG = (static_theta_EEG >= eeg_threshold) * static_theta_EEG
static_alpha_EEG = (static_alpha_EEG >= eeg_threshold) * static_alpha_EEG
static_beta_EEG = (static_beta_EEG >= eeg_threshold) * static_beta_EEG
static_gamma_EEG = (static_broad_EEG >= eeg_threshold) * static_gamma_EEG

# create static connectome
dtype = [("fmri", float), ("broad", float), ("delta", float), ("theta", float), ("alpha", float), ("beta", float), ("gamma", float)]
edge_attr = [static_fMRI, static_broad_EEG, static_delta_EEG, static_theta_EEG, static_alpha_EEG, static_beta_EEG, static_gamma_EEG]

#connectome = nx.from_numpy_array(static_fMRI, create_using=nx.Graph)
static_connectome = nx.Graph()
for i in range(len(static_fMRI)):
    for j in range(len(static_fMRI[0])):
        args = {'u_of_edge': i, 'v_of_edge': j}
        for attr in range(0, len(dtype)):
            weight = (edge_attr[attr])[i][j]
            if weight > 0:
                args[dtype[attr][0]] = weight
        static_connectome.add_edge(**args)

nx.write_edgelist(static_connectome, "data/processed/static_connectome.edges", data=True)

