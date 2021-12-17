#!/bin/python3

import xml.etree.ElementTree as ET
import requests
import time, json, threading

def sottolivello():
	#WRITE THE STATUS CHANGE INTO XML FILE TO UPDATE VALUE ON ZWAY SERVER
	datafile = '/opt/z-way-server/htdocs/liquid_level.xml'
	tree = ET.parse(datafile)
	root = tree.getroot()
	for child in root:
		#print(child.text)
		child.text = 'on'
	tree.write(datafile)
	
def sopralivello():
	#WRITE THE STATUS CHANGE INTO XML FILE TO UPDATE VALUE ON ZWAY SERVER
	datafile = '/opt/z-way-server/htdocs/liquid_level.xml'
	tree = ET.parse(datafile)
	root = tree.getroot()
	for child in root:
		#print(child.text)
		child.text = 'off'
	tree.write(datafile)
		
def livelloliquido():
	threading.Timer(60.0, livelloliquido).start()
	url = 'https://shelly-26-eu.shelly.cloud/device/status'
	ploads = {'id':'XXX', 'auth_key':'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX'}
	r = requests.post(url, data = ploads)
	res = json.loads(r.text)
	list_res = res['data']['device_status']['relays']

	for item in list_res:
		last_state = (item.get('ison'))
		if last_state == True:
			sottolivello()
		else:
			sopralivello()

livelloliquido()