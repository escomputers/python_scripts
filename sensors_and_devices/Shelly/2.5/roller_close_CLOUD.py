#!/bin/python3

import requests
import time

#WAIT FEW SECONDS TO AVOID SHELLY API ERROR 'REQUEST LIMIT REACHED'
time.sleep(2)


#CLOSE DEVICE VIA CLOUD
control_url_close = 'https://shelly-26-eu.shelly.cloud/device/relay/roller/control/'
control_ploads_close = {'direction':'close', 'id':'XXXXXXXX', 'auth_key':'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX'}
control_r_close = requests.post(control_url_close, data = control_ploads_close)

