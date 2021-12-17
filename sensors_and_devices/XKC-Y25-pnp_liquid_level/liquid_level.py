#!/usr/bin/python3

#used sensor xkc-y25-pnp
#vcc (brown) pin sensor 				--> +5V raspi           or --> shelly uni yellow pin
#output (yellow) pin sensor  			--> any GPIO pin raspi  or --> shelly uni white pin
#ground (blue) pin sensor is connected 
#to mode (black) pin sensor 			--> ground pin raspi 	or --> shelly uni green pin

#inside shelly uni web page configuration
#CHANNEL 1 -> ADC AUTOMATION -> ADC 1 ACTION over-adc thresold (mV): 2000 -> over-adc action: relay off
#CHANNEL 1 -> ADC AUTOMATION -> ADC 1 ACTION under-adc thresold (mV): 2000 -> under-adc action: relay on
#repeat for channel 2



import RPi.GPIO as GPIO 
import os, time, threading

def controllo_liquido():
	threading.Timer(10.0, controllo_liquido).start()
	GPIO.setmode(GPIO.BCM)
	GPIO.setup(16, GPIO.IN)
	#GPIO.cleanup()
	if GPIO.input(16):
		print("pin is HIGH")
	else:
		print("pin is LOW")
		
controllo_liquido()