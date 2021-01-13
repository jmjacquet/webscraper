import requests
import json

url = "https://api.datamuse.com/words?ml=jump"
response = requests.get(url)
data = response.content.decode('utf-8')
data_json = json.loads(data)
print(data_json)
data_json = sorted(data,key=lambda x: x['score'])

#print(json.dumps(data_json, indent=4, sort_keys=True))
