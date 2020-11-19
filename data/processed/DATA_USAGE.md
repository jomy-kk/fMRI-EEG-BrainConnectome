.mat 5.0 files have multiple matrices in them. Those are:

`fmri,
broad,
delta,
theta,
alpha,
beta,
gamma`

You can get each by, for e.g:
`(io.loadmat(<mat_file_path>)).get('alpha')`