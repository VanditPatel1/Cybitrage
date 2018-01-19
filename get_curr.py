import json
import requests
import itertools
from API_KEYS import *

BASE_URL = 'https://forex.1forge.com/1.0.2'
QUOTES = '/quotes?pairs='
CURRENCIES = ['USD', 'CAD', 'GBP', 'JPY', 'AUD']
SOURCE = '&source='

def get_curr_combos(currList):

	all_combos = []
	global CURRENCIES
	mix_curr = list(itertools.product(CURRENCIES, CURRENCIES)) #cross all the curriences
	for d_curr in mix_curr:
		if not d_curr[0] == d_curr[1]: #only join diffrent curriences, ignore the same ones
			all_combos.append(''.join(d_curr))

	return all_combos

def get_all_exhange_rates(all_combos):

	all_combos = ','.join(all_combos) #join all currencies in list
	rates = requests.get(BASE_URL + QUOTES + all_combos + API_TOKEN1) #get rates from API
	exhange_rates = json.loads(rates.content) #load into json format
	all_info = json.dumps(exhange_rates, indent=4) #get visuals for print

	return all_info, all_combos

combos = get_curr_combos(CURRENCIES)
a, b = get_all_exhange_rates(combos)

print (a)
