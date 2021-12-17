#!/bin/python3

import requests, os
import json

'''
#GET DEVICE STATUS VIA CLOUD
url = 'https://shelly-26-eu.shelly.cloud/device/status'
ploads = {'id':'XXXXXXX', 'auth_key':'XXXXXXXXXXXXXXXXXX'}
r = requests.post(url, data = ploads)

res = json.loads(r.text)

list_res = res['data']['device_status']['rollers']
'''

#GET DEVICE STATUS VIA LAN
url = 'http://192.168.3.199/roller/0'
r = requests.post(url)

res = json.loads(r.text)

lastdir = res['last_direction']

if lastdir == 'open':
	#RUN CLOSE SCRIPT
	os.system('/usr/bin/python3 /root/shelly_roller_close.py')
else:
	#RUN OPEN SCRIPT
	os.system('/usr/bin/python3 /root/shelly_roller_open.py')
		