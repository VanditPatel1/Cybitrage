import math, urllib2, json, re


def download():
	graph = {}
	page = urllib2.urlopen("http://fx.priceonomics.com/v1/rates/?q=1")
	jsrates = json.loads(page.read())

	pattern = re.compile("([A-Z]{3})_([A-Z]{3})")
	for key in jsrates:
		matches = pattern.match(key)
		conversion_rate = -math.log(float(jsrates[key]))
		from_rate = matches.group(1).encode('ascii','ignore')
		to_rate = matches.group(2).encode('ascii','ignore')
		if from_rate != to_rate:
			if from_rate not in graph:
				graph[from_rate] = {}
			graph[from_rate][to_rate] = float(conversion_rate)
	return graph


d = download()

print (d)

