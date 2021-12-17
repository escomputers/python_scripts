#!/bin/python3

import requests, os
import json, threading


def status_change_on():
	with open('/opt/z-way-server/htdocs/roller.xml', 'w') as f:
		f.write('<item><value>on</value></item>')
		f.close()
	
def status_change_off():
	with open('/opt/z-way-server/htdocs/roller.xml', 'w') as f:
		f.write('<item><value>off</value></item>')
		f.close()
		
def status_change():
	threading.Timer(5.0, status_change).start()
	'''
	#GET DEVICE STATUS VIA CLOUD
	url = 'https://shelly-26-eu.shelly.cloud/device/status'
	ploads = {'id':'XXXXXXXXX', 'auth_key':'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX'}
	r = requests.post(url, data = ploads)
	res = json.loads(r.text)
	'''
	#GET DEVICE STATUS VIA LAN
	url = 'http://192.168.3.199/status'
	r = requests.get(url)
	res = json.loads(r.text)
	list_res = res['rollers']
	for item in list_res:
		lastdir = (item.get('last_direction'))
		if lastdir == 'close':
			status_change_off()
		elif lastdir == 'open':
			status_change_on()


status_change()
