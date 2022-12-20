import requests
headers = {
  'Accept': 'application/json',
  'X-ZAP-API-Key': '148rc7fimunj7pgbg63dbvmlrb'
}


r = requests.get('http://172.28.10.249:8080/JSON/spider/view/status/', params={
}, headers = headers)

print(r.json())