import json
import requests
import itertools
import pandas as pd
import numpy as np
import math
from API_KEYS import *

BASE_URL = 'https://forex.1forge.com/1.0.2'
QUOTES = '/quotes?pairs='
CURRENCIES = ['USD', 'CAD', 'GBP', 'JPY', 'AUD']
SOURCE = '&source='
TIMESTAMP = '???' #set every call

def get_num_currencies(currs):
    return len(currs)

def get_curr_combos(combos):
	all_combos = []
        same = []
	mix_curr = list(itertools.product(combos, combos))      # cross all the curriences
	for d_curr in mix_curr:
		if  d_curr[0] == d_curr[1]:                      # only join different curriences, ignore the same ones
			same.append(''.join(d_curr))

        else: all_combos.append(''.join(d_curr))

        

	return all_combos, same

def get_all_exhange_rates(all_combos):
        print all_combos
        all_combos = ','.join(all_combos)                                       # join all currencies in list
        rates = requests.get(BASE_URL + QUOTES + all_combos + API_TOKEN1)       # get rates from API
        all_info = json.loads(rates.content)                                    # load into json format

        return all_info, all_combos

def edge_val(val):

    return (-1)*math.log(val, 2.0)


def place_in_dict(all_info, all_combos, currs):

        df = pd.DataFrame(all_info)
        df['edge_weight'] = df['price'].apply(edge_val)

        global TIMESTAMP
        TIMESTAMP = df.loc[(0), ('timestamp')]

        for currency in currs:
            d = {'ask': [1], 'bid': [1], 'price': [1], 'symbol':[currency], 'timestamp': TIMESTAMP, 'edge_weight': [0]}
            df2 = pd.DataFrame(data=d)
            df = df.append(df2, ignore_index=True)

        df = df.reset_index(drop=True)
        df = df.sort_values(by=['symbol'])
        df = df.set_index('symbol')
        return df

def get_matrix(df):




def get_data(currs):
	combos, same = get_curr_combos(currs)
	a, b = get_all_exhange_rates(combos)
	df = place_in_dict(a, b, same)

    return df

get_data(CURRENCIES)
