#!/usr/bin/python3

from time import sleep
import RPi.GPIO as GPIO
import os

while True:
	#IF NETWORK INTERFACE IS UP OR DOWN
	wanstate = os.popen('cat /sys/class/net/wan/carrier').read()
	wanstate_int = int(wanstate)
	GPIO.setmode(GPIO.BCM)
	GPIO.setup(25, GPIO.OUT)
	
	if wanstate_int == 1:  
		GPIO.output(25, 1)
	else:      
		GPIO.output(25, 0)
		GPIO.cleanup()