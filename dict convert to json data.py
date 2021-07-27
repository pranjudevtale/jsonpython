import simplejson
city=("ind","d")
city=simplejson.dumps(city)
print(simplejson.loads(city))