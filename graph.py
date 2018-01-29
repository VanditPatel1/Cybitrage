import math
from currs.get_curr_new import *

class weighted_graph:

    def __init__(self, currs):

        self.currencies = currs                                         # list of currencies
        self.curr_df, self.curr_matrix = get_data(currs)                # currency data frame (with listings of all edges)

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
        for currency in curr:
            dist[currency] = float('inf')                  # set all starting vertices to be infinite distance away
            pred[currency] = None

        dist[curr] = 0
        return dist, pred

    def get_val(self, row, column):
        print self.curr_matrix.loc[self.currencies[row], self.currencies[column]]

    def find_arb_opp(self):

        for curr in self.currencies:
            




w = weighted_graph(['USD', 'CAD', 'GBP', 'JPY', 'AUD'])
w.test()
