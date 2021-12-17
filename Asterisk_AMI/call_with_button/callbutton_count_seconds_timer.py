#!/bin/python3
#This script was authored by AndrewH7 and belongs to him (www.instructables.com/member/AndrewH7)
#You have permission to modify and use this script only for your own personal usage
#You do not have permission to redistribute this script as your own work
#Use this script at your own risk

from asterisk.ami import AMIClientAdapter
from asterisk.ami import SimpleAction
from asterisk.ami import AMIClient
from asterisk.ami import EventListener
import RPi.GPIO as GPIO
import smtplib, os, sys, time
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

timespressed = 0
def number():
	global timespressed
	timespressed += 1

while True:
	gpio_pin_number=17
	#Replace YOUR_CHOSEN_GPIO_NUMBER_HERE with the GPIO pin number you wish to use
	#Make sure you know which rapsberry pi revision you are using first
	#The line should look something like this e.g. "gpio_pin_number=7"

	GPIO.setmode(GPIO.BCM)
	#Use BCM pin numbering (i.e. the GPIO number, not pin number)
	#WARNING: this will change between Pi versions
	#Check yours first and adjust accordingly

	GPIO.setup(gpio_pin_number, GPIO.IN, pull_up_down=GPIO.PUD_UP)
	#It's very important the pin is an input to avoid short-circuits
	#The pull-up resistor means the pin is high by default


	GPIO.wait_for_edge(gpio_pin_number, GPIO.FALLING)
	#Use falling edge detection to see if pin is pulled 
	#low to avoid repeated polling

	number()
			

	if timespressed == 1:
		os.system('omxplayer /home/pi/help_voice.wav')
		inizio = time.time()
	if timespressed == 2:
		fine = time.time()
		#do other stuff
		if (fine - inizio < 10):
			client = AMIClient(address='1.1.1.1',port=5038)
			client.login(username='admin',secret='xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx')

			action = SimpleAction(
			'Originate',
			#Channel='SIP/Trunk01111111111111/3333333333', #for external calls using a trunk
			Channel='SIP/6066', #number to call	(destination)
			Exten='6067',		#calling number (source)
			Priority=1,
			Context='default',
			CallerID='Alarm-House',
			)
			def callback_response(response):
				stringa = str(response)
				for line in stringa.split('\n'):
					if 'Success' in line:
						#print(line)
						timespressed = 0
						continue
					elif 'Error' in line:
						#print(line)
						os.system('omxplayer /home/pi/busy.wav')
						#invia email
						sender_address = 'sender@gmail.com'
						sender_pass = '1111'
						recipients = 'test@gmail.com, test2@gmail.com'
						message = MIMEMultipart()
						message['From'] = sender_address
						message['To'] = recipients
						message['Subject'] = 'Call from postbox'
						session = smtplib.SMTP('smtp.gmail.com', 587) 
						session.starttls() 
						session.login(sender_address, sender_pass) #login with mail_id and password
						text = message.as_string()
						session.sendmail(sender_address, recipients.split(','), text)
						session.quit()
						
						timespressed = 0
						continue
			future = client.send_action(action,callback=callback_response)
			response = future.response
			#client.send_action(action)


			timespressed = 0
			continue
		elif (fine - inizio > 10):
			timespressed = 0
			continue