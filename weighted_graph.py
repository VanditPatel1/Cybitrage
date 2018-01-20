import math
from get_curr import *

#################################
## Lets make this into a class ##
##  I think it will be useful  ##
#################################

def create_shortest_path_table(curr):

    global CURRENCIES # TODO replace this later when inputs are a curriencies list
    curr = CURRENCIES # TODO replace this later when inputs are a curriencies list
    distances = {"start" : 0}
    for currency in curr:
        distances[currency] = float("inf")                  #set all starting vertices to be infinite distance away
    for x in distances:
        print (x, distances[x])
    return distances

###############################        BELLMAN-FORD ALGORITHM      ###############################

class weighted_graph:

    def __init__(self, currs):

        self.currencies = currs                             # list of currencies
        self.curr_df = get_data(currs)                      # currency data frame
        #print (self.curr_df)
        self.sp_table = create_shortest_path_table(currs)   # shortest path table

    def get_weight(self, edge):

        edge_rate = self.curr_df.get_value(edge, 'ask')     # edge weights based on 'ask' price
        edge_log_rate = (-1)*math.log(edge_rate, 2.0)       # MUST CONVERT TO LOG-EXCHANGE RATE FOR BELLMAN-FORD
        #print (edge_log_rate)
        return self.curr_df.get_value(edge, 'ask')




test = weighted_graph(['test'])
test.get_weight('USDJPY')
