#!/bin/python3

import xml.etree.ElementTree as ET
import requests, os
import time, json, threading


def powerconsumpt():
	threading.Timer(10.0, powerconsumpt).start()
	'''
	#GET DEVICE STATUS VIA CLOUD
	url = 'https://shelly-26-eu.shelly.cloud/device/status'
	ploads = {'id':'XXXXXX', 'auth_key':'XXXX'}
	r = requests.post(url, data = ploads)
	res = json.loads(r.text)
	list_res = res['data']['device_status']['meters']
	for item in list_res:
		powercons = str(item.get('power'))
		with open('/opt/z-way-server/htdocs/power_meter.html', 'w') as f:
			f.write(powercons)
			f.close()
	'''
	#GET DEVICE STATUS VIA LAN
	url = 'http://192.168.3.193/status'
	r = requests.get(url)
	res = json.loads(r.text)
	list_res = res['meters']
	for item in list_res:
		powercons = str(item.get('power'))
		with open('/opt/z-way-server/htdocs/power_meter.html', 'w') as f:
			f.write(powercons)
			f.close()
			
powerconsumpt()