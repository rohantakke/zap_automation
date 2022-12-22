import requests, json

f = open('config.json')
data = json.load(f)
apiKey = data['api_key']
host = data['listening_host']
port = data['listening_port']

try:
   headers = {
     'Accept': 'application/json',
     'X-ZAP-API-Key': '{}'.format(apiKey)
   }

   r = requests.get('http://{}:{}/JSON/ascan/view/status/'.format(host,port), params={}, headers = headers)

   print(r.json())
except requests.exceptions.ConnectionError as e: 
   print("Failed to establish connection with OWASP ZAP")
   print("Please chech if OWASP ZAP is running.")