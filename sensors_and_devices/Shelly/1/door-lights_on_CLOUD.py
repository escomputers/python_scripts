#!/bin/python3

import requests
import time

#WAIT FEW SECONDS TO AVOID SHELLY API ERROR 'REQUEST LIMIT REACHED'
time.sleep(2)

#VIA LAN
#url = 'http://192.168.89.122/roller/0'
#ploads = {'go':'close'}
#r = requests.get(url, params = ploads)

#print(r.text)
#print(r.url)


#TURN ON DEVICE VIA CLOUD
control_url = 'https://shelly-26-eu.shelly.cloud/device/relay/control/'
control_ploads = {'channel':'0', 'turn':'on', 'id':'f4cfa2ed4adc', 'auth_key':'NWZkZGZ1aWQ4BA003CDE163BEB64810B780D9E49A475236E5413A2A70E01952A9889398E925BCE51C3236FD5FB2'}
control_r = requests.post(control_url, data = control_ploads)

