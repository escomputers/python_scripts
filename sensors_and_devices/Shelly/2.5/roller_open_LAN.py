#!/bin/python3

import requests
import time



#VIA LAN
url = 'http://192.168.3.199/roller/0'
ploads = {'go':'open'}
r = requests.get(url, params = ploads)

#print(r.text)
#print(r.url)


