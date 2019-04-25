import json

with open('figmaoutput.json', 'r') as f:
	x = f.read()
y = json.loads(x)
d = y['document'].items()

for key1 in d:
    for Key2 in d[0]:
        print(key2.children)
