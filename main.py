import numpy as np
import scipy.io as io
from BrainConnectivityToolboxWrapper.Analyser import analyze, plot_relation


input_file = "data/pre-processed/conn_desi_phase_coh_time_fmri.mat"
M_fMRI = np.delete((io.loadmat(input_file)).get('connFMRI'), np.s_[0:3], 2)
static_M_fMRI = np.average(M_fMRI, 2)

analyze(static_M_fMRI, 'fmri')

