#!/bin/python3

import requests
import time

#WAIT FEW SECONDS TO AVOID SHELLY API ERROR 'REQUEST LIMIT REACHED'
time.sleep(2)


#TURN OFF DEVICE VIA CLOUD
control_url_close = 'https://shelly-26-eu.shelly.cloud/device/relay/control/'
control_ploads_close = {'channel':'0', 'turn':'off', 'id':'XXXXX', 'auth_key':'XXXXXXXXXXXXXXXXXX'}
control_r_close = requests.post(control_url_close, data = control_ploads_close)

