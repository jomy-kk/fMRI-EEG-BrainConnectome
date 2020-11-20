import bct
import numpy as np
import scipy.io as io

import statistics


class RichClubCoefficient:
    def __init__(self, graph, name, stats):
        self.g = graph
        self.name = name
        self.stats = stats
        self.binarized = io.loadmat("data/processed/matrices/static_unweighted_adjacency_matrices.mat").get(name)

    # returns a nparray with the degree of each node
    def compute(self):
        # binarize the matrix 1st and pass the binzared to the unweighed. otherwise, it'll all be 0s
        rc_unweighted = bct.rich_club_bu(self.binarized)[0]
        rc_weighted = bct.rich_club_wu(self.g)

        print("Weighted Rich Club Coeff from deg 0 to deg MAX")
        print(np.nan_to_num(rc_weighted))
        print("Unweighted Rich Club Coeff from deg 0 to deg MAX")
        print(np.nan_to_num(rc_unweighted))


        return self.stats
