#!/bin/python3

import xml.etree.ElementTree as ET
import requests
import time, json, threading

def sensoreAperto():
	#WRITE THE STATUS CHANGE INTO XML FILE TO UPDATE VALUE ON ZWAY SERVER
	datafile = '/opt/z-way-server/htdocs/sensor1.xml'
	tree = ET.parse(datafile)
	root = tree.getroot()
	for child in root:
		#print(child.text)
		child.text = 'on'
	tree.write(datafile)
	
def sensoreChiuso():
	#WRITE THE STATUS CHANGE INTO XML FILE TO UPDATE VALUE ON ZWAY SERVER
	datafile = '/opt/z-way-server/htdocs/sensor1.xml'
	tree = ET.parse(datafile)
	root = tree.getroot()
	for child in root:
		#print(child.text)
		child.text = 'off'
	tree.write(datafile)

#via CLOUD
'''
def controllo_sensore():
	threading.Timer(5.0, controllo_sensore).start()
	url = 'https://shelly-26-eu.shelly.cloud/device/status'
	ploads = {'id':'XXXX', 'auth_key':'XXXXXX'}
	r = requests.post(url, data = ploads)
	res = json.loads(r.text)
	list_res = res['data']['device_status']['sensor']
	#for item in list_res:
	#	last_state = (item.get('state'))
	last_state = (list_res["state"])
	if last_state == 'close':
		sensoreChiuso()
	else:
		sensoreAperto()
'''
		
#via LAN (set shelly static IP address)
def controllo_sensore():
	threading.Timer(1.0, controllo_sensore).start()
	url = 'http://192.168.3.191/status'
	#ploads = {'go':'close'}
	r = requests.get(url)

	#print(r.text)
	#print(r.url)
	res = json.loads(r.text)
	list_res = res['sensor']
	last_state = (list_res["state"])
	#for item in list_res:
	#	last_state = (item.get('state'))
	if last_state == 'close':
		sensoreChiuso()
	else:
		sensoreAperto()
			
controllo_sensore()
