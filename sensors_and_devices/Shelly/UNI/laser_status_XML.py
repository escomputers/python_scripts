#!/bin/python3

import xml.etree.ElementTree as ET
import requests
import time, json, threading

def sensore_innescato():
	#WRITE THE STATUS CHANGE INTO XML FILE TO UPDATE VALUE ON ZWAY SERVER
	datafile = '/opt/z-way-server/htdocs/laser_status.xml'
	tree = ET.parse(datafile)
	root = tree.getroot()
	for child in root:
		#print(child.text)
		child.text = 'on'
	tree.write(datafile)
	
def sensore_disinnescato():
	#WRITE THE STATUS CHANGE INTO XML FILE TO UPDATE VALUE ON ZWAY SERVER
	datafile = '/opt/z-way-server/htdocs/laser_status.xml'
	tree = ET.parse(datafile)
	root = tree.getroot()
	for child in root:
		#print(child.text)
		child.text = 'off'
	tree.write(datafile)
		
def controllo_laser():
	threading.Timer(10.0, controllo_laser).start()
	url = 'https://shelly-26-eu.shelly.cloud/device/status'
	ploads = {'id':'XXXXXXXX', 'auth_key':'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX'}
	r = requests.post(url, data = ploads)
	res = json.loads(r.text)
	list_res = res['data']['device_status']['relays']

	for item in list_res:
		last_state = (item.get('ison'))
		if last_state == True:
			sensore_innescato()
		else:
			sensore_disinnescato()

controllo_laser()