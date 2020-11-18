**LEGAL DISCALIMER**

This data is courtesy of Franscisca Ayres Basto Soares Ribeiro to João Miguel Areias Saraiva and João ??? Coelho, and was used solely on the scope of the project of the IST Network Science course in the academic year of 2020-2021.
All the data belongs to one patient whose identity remained anonymous to the developers of this project.

**DATA INFORMATION**

All files in this directory are resting-state, dynamic, functional connectivity matrices of EEG (various rhythms) and fMRI, before a threshold is applied.
The fMRI data was obtained with a TR = 1 second, and the EEG matrices followed the same approach, having a 400 event time series for each, one for each point.
However, a delay of 3 seconds must be taken into account to compare the fMRI with the EEG matrices, i.e, removing the 3 first fMRI time points and the 3 last EEG events, in order to have synchronized matrices.


Source reconstruction was applied to the EEG data, in order to get the time series associated with the same fMRI brain regions, instead of having it associated with each electrode.
Hence, every matrix has a 68x68x400 dimension, being 68 the number of voxels into with the data was divided, according to the cortical regions of the Desikan atlas.


The connectivity of the EEG matrices was computed with the imaginary part of coherency (averaged in windows of 4 seconds). The connectivity of the fMRI matrix was computed with the phase coherence based on the Hilbert transform.

