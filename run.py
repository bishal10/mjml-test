import json
import requests
import sys

# headers = {
#     'X-FIGMA-TOKEN': '11964-dd038e0d-8ac8-4013-a694-e7db037640c4',
# }

# y = requests.get('https://api.figma.com/v1/files/JPkk828iwst6XHzO41jld980', headers=headers).json()

data = sys.argv[1]
token = sys.argv[2]
headers = {
    'X-FIGMA-TOKEN': token,
}

y = requests.get('https://api.figma.com/v1/files/'+ data, headers=headers).json()

for x, y in y.items():
        if x == 'document':
            for a, b in y.items():
                if a == 'children':
                    for c in b:
                        for d,e in c.items():
                            if d == 'children':
                                for f in e:
                                    for g,h in f.items():
                                        if g == 'children':
                                            for i in h:
                                                for j,k in i.items():
                                                    if k == 'layer-1':
                                                        for l,m in i.items():
                                                            if l == 'children':
                                                                for n in m:
                                                                    for o,p in n.items():
                                                                        if p == 'button':
                                                                            for q,r in n.items():
                                                                                if q == 'children':
                                                                                    for s in r:
                                                                                        for t,u in s.items():
                                                                                            if u == 'button-text':
                                                                                                for v,w in s.items():
                                                                                                    if v == 'characters':
                                                                                                        assign_button_text = w
                                                                                                                                                           
with open("base1output.json", "r+") as jsonFile:
    data = json.load(jsonFile)
    for key1, key2 in data.items():
        if key1 == 'children':
            for key3 in key2:
                for key4,key5 in key3.items():
                    if key4 == 'children':
                        for key6 in key5:
                            for key7,key8 in key6.items():
                                if key7 == 'children':
                                    for key9 in key8:
                                        for key10,key11 in key9.items():
                                            if key10 == 'children':
                                                for key12 in key11:
                                                    for key13,key14 in key12.items():
                                                        if key13 == 'children':
                                                            for key15 in key14:
                                                                for key16,key17 in key15.items():
                                                                    if key16 == 'content':
                                                                        key15[key16] = assign_button_text
                                                                    

jsonFile = open("base1output.json", "w+")
jsonFile.write(json.dumps(data))
jsonFile.close()
                                                                                                        
                                                                                                                     
    



    













  




