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
        #rc_weighted = bct.rich_club_wu(self.g)

        print("Unweighted Rich Club Coeff from deg 1 to deg MAX")
        coeffs = np.nan_to_num(rc_unweighted)
        print(coeffs)
        idxs = np.where(coeffs > 0.99)[0] + 1

        #idxs = []
        #added = False
        #for i in range(len(coeffs)):
            #if added:
                #idxs.append(i + 1)
            #if coeffs[i] > 0.99:
                #idxs.append(i + 1)
                #added = True

        print("Degrees in Rich Club:")
        print(idxs)

        self.stats['RichClub'] = self.stats.apply(lambda row: True if row.Degree in idxs else False, axis=1)

        min_deg = idxs[0]

        degs = self.stats['Degree'].to_list()

        c = 0
        for d in degs:
            if d >= min_deg:
                c += 1

        print("Number of nodes in rich club: " + str(c))

        return self.stats, idxs



