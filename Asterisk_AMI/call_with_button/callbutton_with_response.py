#!/bin/python3


from asterisk.ami import AMIClientAdapter
from asterisk.ami import SimpleAction
from asterisk.ami import AMIClient
from asterisk.ami import EventListener
import RPi.GPIO as GPIO
import os, sys, time


while True:
	gpio_pin_number=18
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


	GPIO.wait_for_edge(gpio_pin_number, GPIO.FALLING)
	#Use falling edge detection to see if pin is pulled 
	#low to avoid repeated polling

	client = AMIClient(address='1.1.1.1',port=5038)
	client.login(username='admin',secret='xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx')

	action = SimpleAction(
	'Originate',
	Channel='SIP/Trunk0111111111/3333333333', #for external calls using a trunk
	#Channel='SIP/6066', #number to call (destionation)
	Exten='6066',		#calling number (source)
	Priority=1,
	Context='default',
	CallerID='CustomID',
	)
	def callback_response(response):
		stringa = str(response)
		for line in stringa.split('\n'):
			if 'Success' in line:
				#print('ok')
				continue
			elif 'Error' in line:
				#print('busy')
				continue
	future = client.send_action(action,callback=callback_response)
	response = future.response
	#client.send_action(action)