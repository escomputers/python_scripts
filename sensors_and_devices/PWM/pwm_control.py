#!/usr/bin/python3

from gpiozero import PWMLED
from time import sleep
import requests, json

url = 'http://localhost:8083/ZAutomation/api/v1/devices/DummyDevice_38'
#ploads = {'go':'close'}
r = requests.get(url)
#print(r.text)
#print(r.url)
res = json.loads(r.text)

list_res = res['data']['metrics']

#for item in list_res:
#last_state = (item.get('state'))
livello_pwm = int((list_res["level"]))

livellopwm_def = livello_pwm/100


dispositivo = PWMLED(12)


#dispositivo.value = livellopwm_def


while True:
	dispositivo.value = livellopwm_def
	'''dispositivo.value = 0  # off
	sleep(1)
	dispositivo.value = 0.5  # half brightness
	sleep(1)
	dispositivo.value = 1  # full brightness
	sleep(1)'''
