#!/usr/bin/env python
import time, json, requests
from zapv2 import ZAPv2


def run_spider():	
	f = open('config.json')
	data = json.load(f)

	target = data['target_url']
	apiKey = data['api_key']
	host = data['listening_host']
	port = data['listening_port']

	zap = ZAPv2(apikey=apiKey, proxies={'http': 'https://{}:{}'.format(host,port), 'https': 'http://{}:{}'.format(host,port)})

	print('Spidering target {}'.format(target))
	# The scan returns a scan id to support concurrent scanning
	scanID = zap.spider.scan(target)
	while int(zap.spider.status(scanID)) < 100:
		print('Spider progress %: {}'.format(zap.spider.status(scanID)))
		time.sleep(8)
	print('Spider has completed!')
	f.close()

try:
   run_spider()
except requests.exceptions.ConnectionError as e:    # This is the correct syntax
   print(e)
   print("Please chech if OWASP ZAP is running.")