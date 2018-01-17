import pprint
import json
import requests
from API_KEYS import *

BASE_URL = 'http://apilayer.net/api'

#list of all curriences
res = requests.get(BASE_URL + '/list' + API_TOKEN1)

#print (str(json.loads(res.text)).encode("utf-8")) BELOW IS A SIMPLER WAY TO DO THIS
print (str(res.json()).encode("utf-8"))


### '/list' returns all curriences supported
LIST = '/list'
