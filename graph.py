import math
from get_curr import *


class arbitrage:

    def __init__(self, cur):
        if cur:
            self.currs = cur
        else:
            cur = ['USD', 'CAD', 'GBP', 'JPY', 'AUD']
            print ("No curriences provided, default used")

        self.cur_df = get_data(cur) #init df with all import values
        print self.cur_df

    def distance_calc(self, a, b):
        total = self.cur_df['price'][a] + self.cur_df['price'][b]
        return total

    def dist_matrix(self):
        print self.cur_df

    def arb_opp(self):

        ll = 0
        for x in range(0, len(self.currs)):
            for y in range(0, len(self.currs)):
                for z in range(0, len(self.currs)):
                    if self.distance_calc(y, z) > \
                        self.distance_calc(y, x) + self.distance_calc(x, y):
                        total = self.distance_calc(y, x) + self.distance_calc(x, y)
                        #print total
                        ll = ll+1
                        print ll





x = arbitrage(['USD', 'CAD', 'GBP', 'JPY', 'AUD'])
x.dist_matrix()
