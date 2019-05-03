import json
import requests
headers = {
    'X-FIGMA-TOKEN': '11964-dd038e0d-8ac8-4013-a694-e7db037640c4',
}

y = requests.get('https://api.figma.com/v1/files/JPkk828iwst6XHzO41jld980', headers=headers).json()
print(y)

# with open('new_figma_json.json', 'r') as f:
# 	x = f.read()
# y = json.loads(x)
# print(y

# import json
# import requests
# import sys

# data = sys.argv[1]
# token = sys.argv[2]
# headers = {
#     'X-FIGMA-TOKEN': token,
# }

# y = requests.get('https://api.figma.com/v1/files/'+ data, headers=headers).json()
# # for a in sys.argv:
#     # print(sys.argv(a))
# print(y))