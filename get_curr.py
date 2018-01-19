import json
import requests
import itertools
import pandas as pd
from API_KEYS import *

BASE_URL = 'https://forex.1forge.com/1.0.2'
QUOTES = '/quotes?pairs='
CURRENCIES = ['USD', 'CAD', 'GBP', 'JPY', 'INR']
SOURCE = '&source='

def get_all_exhange_rates(all_combos):

        all_combos = ','.join(all_combos) #join all currencies in list
        rates = requests.get(BASE_URL+QUOTES+all_combos+API_TOKEN1) #get rates from API
        all_info = json.loads(rates.content) #load into json format
        #all_info = json.dumps(exhange_rates, indent=4) #get visuals for print

        return all_info, all_combos


def mix_curr(currList):

        all_combos = []
        mix_curr = list(itertools.product(currList, currList)) #cross all the curriences
        for d_curr in mix_curr:
                if not d_curr[0] == d_curr[1]: #only join diffrent curriences, ignore the same ones
                        all_combos.append(''.join(d_curr))

        return all_combos


def place_in_dict(all_info, all_combos):
        df = pd.DataFrame(all_info)
        return df


def get_data():
	combos = mix_curr(CURRENCIES)
	a, b = get_all_exhange_rates(combos)
	df = place_in_dict(a, b)
	return df
