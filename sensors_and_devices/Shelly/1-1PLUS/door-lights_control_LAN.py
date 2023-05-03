#!/bin/python3

import requests
import time

#IF CONNECTED TO A DOOR, SET AUTO-OFF TIMER INTO SHELLY 1 WEB PAGE CONFIGURATION
#VIA LAN
url = 'http://192.168.3.192/relay/0/'
ploads = {'turn':'on'}
r = requests.get(url, params = ploads)

#print(r.text)
#print(r.url)



