import json

print open("json.json").readline()

data = json.loads(open("json.json").readline())

print data