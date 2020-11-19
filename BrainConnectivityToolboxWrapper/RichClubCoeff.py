import bct

import statistics


class RichClubCoefficient:
    def __init__(self, graph, name, stats):
        self.g = graph
        self.name = name
        self.stats = stats

    # returns a nparray with the degree of each node
    def compute(self):
        # binarize the matrix 1st and pass the binzared to the unweighed. otherwise, it'll all be 0s
        rc_unweighted = bct.rich_club_bu(self.g)[0]
        #rc_weighted = bct.rich_club_wu(self.g)

        self.stats['RichClub Unweighted'] = [v for v in rc_unweighted]
        #self.stats['RichClub Weighted'] = [v for v in rc_weighted]

        return self.stats


#for some reason the weighted rich club is returning all NAN
