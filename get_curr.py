import json
import requests
from API_KEYS import *

BASE_URL = 'http://apilayer.net/api'

### '/list' returns all curriences supported
LIST = '/list'

#list of all curriences
#res = requests.get(BASE_URL + LIST + API_TOKEN1)
##print (str(json.loads(res.text)).encode("utf-8")) BELOW IS A SIMPLER WAY TO DO THIS
#print (str(res.json()).encode("utf-8"))

currencies = [] #stores a copy of the currencies which will be used (for the API)

#copy the list of currencies into variable currencies
def get_currencies(copy):
    global currencies
    currencies = copy

#create the currency exchange values as directed edges of the graph and return as array or something
def create_edges():
