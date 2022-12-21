#!/usr/bin/env python
import time, json
from pprint import pprint
from zapv2 import ZAPv2

def launch_active_scan():
    f = open('config.json')
    data = json.load(f)
    target = data['target_url']
    apiKey = data['api_key']
    host = data['listening_host']
    port = data['listening_port']

    zap = ZAPv2(apikey=apiKey, proxies={'http': 'https://{}:{}'.format(host,port), 'https': 'http://{}:{}'.format(host,port)})

    # TODO : explore the app (Spider, etc) before using the Active Scan API, Refer the explore section
    print('Active Scanning target {}'.format(target))
    scanID = zap.ascan.scan(target)
    while int(zap.ascan.status(scanID)) < 100:
        # Loop until the scanner has finished
        print('Scan progress %: {}'.format(zap.ascan.status(scanID)))
        time.sleep(5)

    print('Active Scan completed')
    # Print vulnerabilities found by the scanning
    print('Hosts: {}'.format(', '.join(zap.core.hosts)))
    print('Alerts: ')
    pprint(zap.core.alerts(baseurl=target))