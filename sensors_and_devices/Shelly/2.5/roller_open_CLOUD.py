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

#OPEN DEVICE VIA CLOUD
control_url_open = 'https://shelly-26-eu.shelly.cloud/device/relay/roller/control/'
control_ploads_open = {'direction':'open', 'id':'8caab561e87c', 'auth_key':'NWZkZGZ1aWQ4BA003CDE163BEB64810B780D9E49A475236E5413A2A70E01952A9889398E925BCE51C3236FD5FB2'}
control_r_open = requests.post(control_url_open, data = control_ploads_open)

