import json
import requests

headers = {
    'X-FIGMA-TOKEN': '11964-dd038e0d-8ac8-4013-a694-e7db037640c4',
}

response = requests.get('https://api.figma.com/v1/files/JPkk828iwst6XHzO41jld980', headers=headers).json()

# Encode the Python dictionary into a JSON string.
new_json_string = json.dumps(response, indent=4)
#print(new_json_string)


f = open( 'fout.json', 'w' )
f.write(new_json_string)
f.close()

