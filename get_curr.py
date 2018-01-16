import json
import requests

API_TOKEN1 = '?access_key=78022fdcef4149740ce787258b37ade7'
API_TOKEN2 = '?access_key=c4449a03fbc0f02110afcafa7e05043b'
BASE_URL = 'http://apilayer.net/api'

#list of all curriences
res = requests.get(BASE_URL+'/list' + API_TOKEN1)

print json.loads(res.text)



### '/list' returns all curriences supported
LIST = '/list'

