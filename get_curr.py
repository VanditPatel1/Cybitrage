import json
import requests
import itertools
import pandas as pd
from API_KEYS import *

BASE_URL = 'https://forex.1forge.com/1.0.2'
QUOTES = '/quotes?pairs='
CURRENCIES = ['USD', 'CAD', 'GBP', 'JPY', 'AUD']
SOURCE = '&source='

def get_num_currencies(currs):
    currs = CURRENCIES
    return len(currs)

def get_curr_combos(combos):
	combos = CURRENCIES #replace this later when inputs are a curriencies list
	all_combos = []
	mix_curr = list(itertools.product(combos, combos)) #cross all the curriences
	for d_curr in mix_curr:
		if not d_curr[0] == d_curr[1]: #only join diffrent curriences, ignore the same ones
			all_combos.append(''.join(d_curr))
	
	return all_combos

def get_all_exhange_rates(all_combos):

        all_combos = ','.join(all_combos) #join all currencies in list
        rates = requests.get(BASE_URL + QUOTES + all_combos + API_TOKEN1) #get rates from API
        all_info = json.loads(rates.content) #load into json format
        #all_info = json.dumps(exhange_rates, indent=4) #get visuals for print

        return all_info, all_combos

def place_in_dict(all_info, all_combos):
        df = pd.DataFrame(all_info)
        df = df.sort_values(by=['symbol'])
        df = df.reset_index(drop=True)
        df = df.set_index('symbol')
        return df

def get_data(currs):
	combos = get_curr_combos(currs)
	a, b = get_all_exhange_rates(combos)
	df = place_in_dict(a, b)
	return df
