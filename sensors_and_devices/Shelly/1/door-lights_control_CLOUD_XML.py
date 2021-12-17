#!/bin/python3

import xml.etree.ElementTree as ET
import requests, os
import json, time

#GET DEVICE STATUS VIA CLOUD
url = 'https://shelly-26-eu.shelly.cloud/device/status'
ploads = {'id':'XXXXXXXXXXXXXXXX', 'auth_key':'XXXXXXXXXXXXXXXXXXXXXXX'}
r = requests.post(url, data = ploads)

res = json.loads(r.text)

list_res = res['data']['device_status']['relays']


for item in list_res:
	last_state = (item.get('ison'))
	if last_state == True:
		#RUN CLOSE SCRIPT
		os.system('/usr/bin/python3 /root/shelly_lights_off.py')
		time.sleep(1)
		#WRITE THE STATUS CHANGE INTO XML FILE TO UPDATE VALUE ON ZWAY SERVER
		datafile = '/opt/z-way-server/htdocs/lights.xml'
		tree = ET.parse(datafile)
		root = tree.getroot()
		for child in root:
			#print(child.text)
			child.text = 'off'
		tree.write(datafile)
	else:
		#RUN OPEN SCRIPT
		os.system('/usr/bin/python3 /root/shelly_lights_on.py')
		time.sleep(1)
		#WRITE THE STATUS CHANGE INTO XML FILE TO UPDATE VALUE ON ZWAY SERVER
		datafile = '/opt/z-way-server/htdocs/lights.xml'
		tree = ET.parse(datafile)
		root = tree.getroot()
		for child in root:
			#print(child.text)
			child.text = 'on'
		tree.write(datafile)