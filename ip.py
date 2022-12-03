


import json
import requests
api_url = 'https://www.virustotal.com/vtapi/v2/ip-address/report'
params = dict(apikey='ce67285c4e31732904d998789737b6419ef21b3dd73f4af53751fcdb8a3820b4', ip='192.10.1.10')
response = requests.get(api_url, params=params)
if response.status_code == 200:
  result=response.json()
  print(json.dumps(result, sort_keys=False, indent=4))
    
