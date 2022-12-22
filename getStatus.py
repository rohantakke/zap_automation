import requests
try:
   headers = {
     'Accept': 'application/json',
     'X-ZAP-API-Key': '148rc7fimunj7pgbg63dbvmlrb'
   }

   r = requests.get('http://127.0.0.1:8082/JSON/ascan/view/status/', params={}, headers = headers)

   print(r.json())
except requests.exceptions.ConnectionError as e:    # This is the correct syntax
   print("Failed to establish connection with OWASP ZAP")
   print("Please chech if OWASP ZAP is running.")