#!/bin/python3

import xml.etree.ElementTree as ET
import requests
import time, json, threading

def pir_innescato():
	try:
		#WRITE THE STATUS CHANGE INTO XML FILE TO UPDATE VALUE ON ZWAY SERVER
		datafile = '/opt/z-way-server/htdocs/pir1.xml'
		tree = ET.parse(datafile)
		root = tree.getroot()
		for child in root:
			child.text = 'on'
		tree.write(datafile)
	except:
		pass

def pir_disinnescato():
	try:
		#WRITE THE STATUS CHANGE INTO XML FILE TO UPDATE VALUE ON ZWAY SERVER
		datafile = '/opt/z-way-server/htdocs/pir1.xml'
		tree = ET.parse(datafile)
		root = tree.getroot()
		for child in root:
			child.text = 'off'
		tree.write(datafile)
	except:
		pass
		
def controllo_pir():
	threading.Timer(1.0, controllo_pir).start()
	url = 'https://shelly-26-eu.shelly.cloud/device/status'
	ploads = {'id':'XXXXXXXXXXXXXXX', 'auth_key':'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX'}
	r = requests.post(url, data = ploads)
	res = json.loads(r.text)
	
	list_res = res['data']['device_status']['relays']

	for item in list_res:
		last_state = (item.get('ison'))
		if last_state == True:
			pir_innescato()
			time.sleep(7)
		else:
			pir_disinnescato()

controllo_pir()