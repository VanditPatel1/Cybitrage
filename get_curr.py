import json
import requests
from API_KEYS import *

BASE_URL = 'http://apilayer.net/api'

#list of all curriences
res = requests.get(BASE_URL+'/list' + API_TOKEN1)

print json.loads(res.text)



### '/list' returns all curriences supported
LIST = '/list'

