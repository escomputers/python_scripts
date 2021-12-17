#!/bin/python3

import xml.etree.ElementTree as ET
import requests
import time, json, threading

def status220v_change_on():
	#WRITE THE STATUS CHANGE INTO XML FILE TO UPDATE VALUE ON ZWAY SERVER
	datafile = '/opt/z-way-server/htdocs/220V_status.xml'
	tree = ET.parse(datafile)
	root = tree.getroot()
	for child in root:
		#print(child.text)
		child.text = 'on'
	tree.write(datafile)
	
def status220v_change_off():
	#WRITE THE STATUS CHANGE INTO XML FILE TO UPDATE VALUE ON ZWAY SERVER
	datafile = '/opt/z-way-server/htdocs/220V_status.xml'
	tree = ET.parse(datafile)
	root = tree.getroot()
	for child in root:
		#print(child.text)
		child.text = 'off'
	tree.write(datafile)
		
def status220v_change():
	threading.Timer(60.0, status220v_change).start()
	url = 'https://shelly-26-eu.shelly.cloud/device/status'
	ploads = {'id':'XXXXXXXXX', 'auth_key':'XXXX'}
	r = requests.post(url, data = ploads)
	res = json.loads(r.text)
	list_res = res['data']['device_status']['relays']

	for item in list_res:
		last_state = (item.get('ison'))
		if last_state == True:
			status220v_change_on()
		else:
			status220v_change_off()

status220v_change()