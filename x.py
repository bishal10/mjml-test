import json

with open('figmaoutput.json', 'r') as f:
	x = f.read()
y = json.loads(x)
#print(y)
with open('finaloutput.json', 'r') as o:
        a = o.read()
print(a)
c = b = json.loads(a)



if y["document"]["children"][0]["children"][0]["name"] == "hello world":
	c["children"][0]["children"][0]["children"][0]["children"][0]["children"][0]["content"] = "hello world"
	#b.update(b["children"][0]["children"][0]["children"][0]["children"][0]["children"][0]["content"] = "hello world")
	b.update(c)
	
print(b)
#f.write(b)
#f.close()
