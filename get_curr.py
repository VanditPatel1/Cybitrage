import json
import requests
from API_KEYS import *

BASE_URL = 'http://apilayer.net/api'
LIVE = '/live' #for live results
CURRENCIES = '&currencies='
SOURCE = '&source='
FORMAT = '&format=1'
LIST = '/list' 
LIST_CURR = ['CAD', 'JPY', 'INR', 'GBP', 'AUD', 'USD']

print BASE_URL+LIVE+API_TOKEN1+CURRENCIES+','.join(LIST_CURR)

def USD_Exchanges():
	rates = requests.get(BASE_URL+LIVE+API_TOKEN1+CURRENCIES+','.join(LIST_CURR)+SOURCE+'USD'+FORMAT)
	print rates.text

USD_Exchanges()


#list of all curriences
#res = requests.get(BASE_URL + LIST + API_TOKEN1)
##print (str(json.loads(res.text)).encode("utf-8")) BELOW IS A SIMPLER WAY TO DO THIS
#print (str(res.json()).encode("utf-8"))

currencies = [] #stores a copy of the currencies which will be used (for the API)

#copy the list of currencies into variable currencies
#def get_currencies(copy):
#    global currencies
#    currencies = copy

#create the currency exchange values as directed edges of the graph and return as array or something
#def create_edges():
