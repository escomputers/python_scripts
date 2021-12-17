#!/usr/bin/python3

from gpiozero import PWMLED
from time import sleep
import requests, json


'''
https://www.tindie.com/products/next_evo1/universal-ac-mains-dimmer-mpdmv41/
'''

url = 'http://localhost:8083/ZAutomation/api/v1/devices/DummyDevice_38'
#ploads = {'go':'close'}
r = requests.get(url)
#print(r.text)
#print(r.url)
res = json.loads(r.text)

list_res = res['data']['metrics']

pwm_level = int((list_res["level"]))

pwm_level_def = pwm_level/100


device = PWMLED(12)

while True:
	device.value = pwm_level_def
	'''
	device.value = 0  # off
	sleep(1)
	device.value = 0.5  # half brightness
	sleep(1)
	device.value = 1  # full brightness
	sleep(1)'''
