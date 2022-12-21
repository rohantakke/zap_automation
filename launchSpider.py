#!/usr/bin/env python
import time, json
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
		# Poll the status until it completes
		print('Spider progress %: {}'.format(zap.spider.status(scanID)))
		time.sleep(3)

	print('Spider has completed!')
	# Prints the URLs the spider has crawled
	print('\n'.join(map(str, zap.spider.results(scanID))))
	f.close()