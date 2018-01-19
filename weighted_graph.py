import math
from get_curr import *

###############################
##Lets make this into a class##
###I think it will be useful###
###############################

#Look-Up Table for Edge Weights
#edges = get_data() #why is this a global?

def create_shortest_path_table():

    global CURRENCIES
    distances = {}
    for curr in list(edges.index.values):
        distances[curr] = float("inf") #set all starting vertices to be infinite distance away
    return distances

def get_weight(currency):
    #global edges
    #edges = get_data() #we can get the frame here
	
    return edges.get_value(currency, 'ask') #returns edge weights based on 'ask' price

#BELLMAN-FORD ALGORITHM
#create_shortest_path_table()




class weighted_graph:
	def __init__(self, currs):
		curr_df = get_data(currs)
		print curr_df


test = weighted_graph('test')	
