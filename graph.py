import math
from currs.get_curr_new import *


class weighted_graph:

    def __init__(self, currs):

        self.currencies = currs                                         # list of currencies
        self.curr_df, self.curr_matrix = get_data(currs)                # currency data frame (with listings of all edges)

        print (self.currencies)

    def dist_pred_dict(self, curr):
        """
        Init each vertex to have a
        distance of inf from each other,
        have a predecessor of None and
        set source curr, in varible 'curr'
        to 0
        """
        dist = {}
        pred = {}
        for currency in self.currencies:
            dist[currency] = float('inf')                  # set all starting vertices to be infinite distance away
            pred[currency] = None

        dist[curr] = 0

        return dist, pred


    def get_weight(self, row, column):
        return self.curr_matrix.loc[row, column]


    def relax(self, node, next, dist, pred):

        if dist[next] > dist[node] + self.get_weight(node, next):
            dist[next] = dist[node] + self.get_weight(node, next)
            pred[next] = node

    def find_arb_opp(self):

        for to_curr in self.currencies:
            dist, pred = self.dist_pred_dict(to_curr)

            for x in range(0, len(self.currencies)-1):
                for u in self.currencies:
                    for v in self.currencies:
                        relax(u, v, dist, pred)





w = weighted_graph(['USD', 'CAD', 'GBP', 'JPY', 'AUD'])
w.find_arb_opp()
