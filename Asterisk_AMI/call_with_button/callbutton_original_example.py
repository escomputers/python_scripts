#!/bin/python
#This script was authored by AndrewH7 and belongs to him (www.instructables.com/member/AndrewH7)
#You have permission to modify and use this script only for your own personal usage
#You do not have permission to redistribute this script as your own work
#Use this script at your own risk

from asterisk.ami import *
import RPi.GPIO as GPIO
import os

while True:
	gpio_pin_number=22
	#Replace YOUR_CHOSEN_GPIO_NUMBER_HERE with the GPIO pin number you wish to use
	#Make sure you know which rapsberry pi revision you are using first
	#The line should look something like this e.g. "gpio_pin_number=7"

	GPIO.setmode(GPIO.BOARD)
	#Use BCM pin numbering (i.e. the GPIO number, not pin number)
	#WARNING: this will change between Pi versions
	#Check yours first and adjust accordingly

	GPIO.setup(gpio_pin_number, GPIO.IN, pull_up_down=GPIO.PUD_UP)
	#It's very important the pin is an input to avoid short-circuits
	#The pull-up resistor means the pin is high by default

	try:
		GPIO.wait_for_edge(gpio_pin_number, GPIO.FALLING)
		#Use falling edge detection to see if pin is pulled 
		#low to avoid repeated polling

		client = AMIClient(address='1.1.1.1',port=5038)
		client.login(username='admin',secret='xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx')

		adapter = AMIClientAdapter(client)
		adapter.Originate(
		Channel='SIP/Trunk01111111111111/3333333333', #for external calls using a trunk
		Channel='SIP/6066', #number to call	(destination)
		Exten='6067',		#calling number (source)
		Priority=1,
		Context='default',
		CallerID='Alarm-House',
		)
		client.send_action(action)
	except:
		pass

GPIO.cleanup()
#Revert all GPIO pins to their normal states (i.e. input = safe)
