import math
from get_curr_new import *

#################################
## Lets make this into a class ##
##  I think it will be useful  ##
#################################

def create_distance_table(curr):

    global CURRENCIES                                       # TODO replace this later when inputs are a curriencies list
    curr = CURRENCIES                                       # TODO replace this later when inputs are a curriencies list
    distances = {}
    for currency in curr:
        distances[currency] = float('inf')                  # set all starting vertices to be infinite distance away
    # for x in distances:
    #     print (x, distances[x])
    return distances

def create_predecessor_table(curr):

    global CURRENCIES                                       # TODO replace this later when inputs are a curriencies list
    curr = CURRENCIES                                       # TODO replace this later when inputs are a curriencies list
    predecessor = {}
    for currency in curr:
        predecessor[currency] = None                        #set all starting vertices to have no predecessor
    # for x in predecessor:
    #     print (x, predecessor[x])
    return predecessor

###############################        BELLMAN-FORD ALGORITHM      ###############################

class weighted_graph:

    def __init__(self, currs):

        self.currencies = currs                             # list of currencies
        self.curr_df, self.curr_matrix = get_data(currs)    # currency data frame (with listings of all edges)
        print (self.curr_df)
        print ('------------')
        print (self.curr_matrix)
        #print ('HELLO' + str(self.curr_matrix[AUD][AUD]))
        self.dist_table = create_distance_table(currs)      # shortest path table
        self.pre_table = create_predecessor_table(currs)    # predecessor table

    def get_weight(self, edge):

        edge_rate = self.curr_df.get_value(edge, 'ask')     # edge weights based on 'ask' price
        edge_log_rate = (-1)*math.log(edge_rate, 2.0)       # MUST CONVERT TO LOG-EXCHANGE RATE FOR BELLMAN-FORD
        #print (edge_log_rate)
        return edge_log_rate

    def has_arbitrage_opportunity(self):

        updated = True                                                  # keeps track of whether an update was made or not
        iteration = 1                                                   # keeps track of the iteration number
        num_currencies = len(self.currencies)                           # number of currencies
        currency_list = ['STA'] + self.currencies                       # temp list to store currencies + STA node
        has_arbitrage = False                                           # keeps track of whether arbitrage exists

        # FIRST |V-1| ITERATIONS
        while iteration < num_currencies and updated == True:

            updated = False                                             # reset updated for checking if an update occurs later
            for from_curr in currency_list:                             # First Loop for each currency

                for to_curr in currency_list:                           # Second Loop for each currency that...

                    if (to_curr != from_curr and to_curr != 'STA'):     # ... is a different currency than the first (and is not STA)

                        if self.dist_table[from_curr] + self.get_weight(from_curr + to_curr) < self.dist_table[to_curr]:         # if a shorter path is found to THIS node

                            self.dist_table[to_curr] = self.dist_table[from_curr] + self.get_weight(from_curr + to_curr)         # update distance table with shorter path distance
                            self.pre_table[to_curr] = from_curr                                                                  # update predecessor table with shorter path node
                            updated = True                                                                                       # an update occurred so updated = True

            iteration = iteration + 1

        # FINAL |V-1| ITERATIONS to detect NEGATIVE WEIGHT CYCLES
        if updated == True:

            iteration = 1
            while iteration < num_currencies and updated == True:

                updated = False
                for from_curr in self.currencies:                           # First Loop for each currency
                    for to_curr in self.currencies:                         # Second Loop for each currency that...
                        if (to_curr != from_curr and to_curr != 'STA'):     # ... is a different currency than the first (and is not STA)

                            if self.dist_table[from_curr] + self.get_weight(from_curr + to_curr) < self.dist_table[to_curr]:    # negative cycle detected

                                self.dist_table[to_curr] = float("-inf")                                                        # update distance table with -infinity
                                self.pre_table[to_curr] = from_curr                                                             # update predecessor table with shorter path node
                                updated = True
                                has_arbitrage = True

        return has_arbitrage

    def show_arbitrage_opportunity(self):

        arbitrage_currencies = self.currencies                      # temp list used to display currencies with arbitrage opportunities

        if self.has_arbitrage_opportunity():

            for currency in arbitrage_currencies:
                print ('??' + currency + ': ' + str(self.dist_table[currency]))
                if self.dist_table[currency] != float("-inf"):      # no arbitrage opportunity detected
                    print ('??' + currency + ': ' + str(self.dist_table[currency]))
                    arbitrage_currencies.remove(currency)           # remove currency from list of currencies with arbitrage opportunities

            # for currency in arbitrage_currencies:
            #     predecessor = pre_table[currency]                 # first predecessor in arbitrage cycle
            #     while predecessor != currency:                    # while the cycle hasn't looped to beginning

        else:
            arbitrage_currencies = []

        for i in arbitrage_currencies:
            print('----------------------')
            print (i)
        return (arbitrage_currencies)




test = weighted_graph(['USD', 'CAD', 'GBP', 'JPY', 'AUD'])
test.show_arbitrage_opportunity()
print ('+++++++++++++++++++++++++++')               # FOR TESTING
print (test.dist_table)                             # FOR TESTING
print ('**************************')                # FOR TESTING
print (test.pre_table)                              # FOR TESTING
test.get_weight('USDJPY')
