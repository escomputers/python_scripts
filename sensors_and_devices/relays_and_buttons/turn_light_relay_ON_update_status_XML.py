#!/usr/bin/python3

import xml.etree.ElementTree as ET
from time import sleep
import RPi.GPIO as GPIO

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
#GPIO.setmode(GPIO.BCM)
GPIO.setup(16, GPIO.OUT)
GPIO.output(16, 1)

datafile = '/opt/z-way-server/htdocs/lights_state.xml'
tree = ET.parse(datafile)
root = tree.getroot()
for child in root:
	#print(child.text)
	child.text = 'on'
tree.write(datafile)