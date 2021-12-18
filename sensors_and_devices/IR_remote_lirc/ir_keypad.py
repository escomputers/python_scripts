#!/usr/bin/python3

import time, os
import socket, re
from simplecrypto import encrypt
import RPi.GPIO as GPIO

def passiveBuzzer():
	#Set trigger PIN according with your cabling
	triggerPIN = 23
	GPIO.setwarnings(False) 
	GPIO.setmode(GPIO.BCM)
	GPIO.setup(triggerPIN,GPIO.OUT)
	buzzer = GPIO.PWM(triggerPIN, 800) #Set frequency to 1 Khz
	buzzer.start(50) #Set dutycycle to 10
	#this row makes buzzer work for 1 second, then
	#cleanup will free PINS and exit will terminate code execution
	time.sleep(0.3)
	#commands to change frequency and
	#dutycycle without stopping buzzer, or to stop buzzer:
	#buzzer.ChangeDutyCycle(10)
	#buzzer.ChangeFrequency(1000)
	#buzzer.stop()


def doublepassiveBuzzer():
	#Set trigger PIN according with your cabling
	triggerPIN = 23
	GPIO.setwarnings(False) 
	GPIO.setmode(GPIO.BCM)
	GPIO.setup(triggerPIN,GPIO.OUT)
	buzzer = GPIO.PWM(triggerPIN, 1300) #Set frequency to 1 Khz
	buzzer.start(50) #Set dutycycle to 10
	time.sleep(0.3)
	#buzzer.ChangeDutyCycle(1)
	buzzer.ChangeFrequency(800)
	time.sleep(0.3)
	buzzer.stop()

def longpassiveBuzzer():
	#Set trigger PIN according with your cabling
	triggerPIN = 23
	GPIO.setwarnings(False) 
	GPIO.setmode(GPIO.BCM)
	GPIO.setup(triggerPIN,GPIO.OUT)
	buzzer = GPIO.PWM(triggerPIN, 1000) #Set frequency to 1 Khz
	buzzer.start(1) #Set dutycycle to 10
	#this row makes buzzer work for 1 second, then
	#cleanup will free PINS and exit will terminate code execution
	time.sleep(0.6)

def whitePin():
	#turn GREEN ON
	os.system('gpio mode 1 out')
	os.system('gpio write 1 0')
	#turn RED ON
	os.system('gpio mode 0 out')
	os.system('gpio write 0 0')
	#turn BLUE ON
	os.system('gpio mode 2 out')
	os.system('gpio write 2 0')
	time.sleep(0.3)
	cleanPins()
	
def cleanPins():
	#turn GREEN OFF
	os.system('gpio mode 1 out')
	os.system('gpio write 1 1')
	#turn RED OFF
	os.system('gpio mode 0 out')
	os.system('gpio write 0 1')
	#turn BLUE OFF
	os.system('gpio mode 2 out')
	os.system('gpio write 2 1')

def redPin():
	#turn BLUE OFF
	os.system('gpio mode 2 out')
	os.system('gpio write 2 1')
	#turn GREEN OFF
	os.system('gpio mode 1 out')
	os.system('gpio write 1 1')
	#turn RED ON
	os.system('gpio mode 0 out')
	'''p = GPIO.PWM(11, 50)  # channel=11 frequency=50Hz
	p.start(0)'''
	os.system('gpio write 0 0')

def greenPin():
	#turn BLUE OFF
	os.system('gpio mode 2 out')
	os.system('gpio write 2 1')
	#turn RED OFF
	os.system('gpio mode 0 out')
	os.system('gpio write 0 1')
	#turn GREEN ON
	os.system('gpio mode 1 out')
	os.system('gpio write 1 0')
	
def bluePin():
	#turn GREEN OFF
	os.system('gpio mode 1 out')
	os.system('gpio write 1 1')
	#turn RED OFF
	os.system('gpio mode 0 out')
	os.system('gpio write 0 1')
	#turn BLUE ON
	os.system('gpio mode 2 out')
	os.system('gpio write 2 0')
	
	

SOCKPATH = "/var/run/lirc/lircd"

sock = None

#Establish a socket connection to the lirc daemon
def init_irw():
	global sock
	sock = socket.socket(socket.AF_UNIX, socket.SOCK_STREAM)
	sock.connect(SOCKPATH)
	#print ('Socket connection established!')
	#print ('Ready...')

#parse the output from the daemon socket
def getKey():
	while True:
		data = sock.recv(128)
		data = data.strip()

		if (len(data) > 0):
			break

	words = data.split()
	clean_words = (words[2])
	a = (words[2]).decode()
	values = (a.split("_",1)[1])
	return values


code1 = '2013'
code2 = '2021'
code3 = '8889'
def controller():
			keys = []
			ts_list = []
			timediff1 = 0
			timediff2 = 0
			timediff3 = 0
			ts_digit1 = 0
			ts_digit2 = 0
			ts_digit3 = 0
			ts_digit4 = 0
			
			keys.append(getKey())
			passiveBuzzer()
			bluePin()
			now1 = time.localtime() # get struct_time
			ts_digit1 = time.strftime("%H%M%S", now1)
			ts_list.append(1)


			keys.append(getKey())
			passiveBuzzer()
			bluePin()
			now2 = time.localtime() # get struct_time
			ts_digit2 = time.strftime("%H%M%S", now2)
			ts_list.append(2)

			timediff1 = int(ts_digit2) - int(ts_digit1)
			
			if timediff1 >= 2:
				redPin()
				longpassiveBuzzer()
				time.sleep(2)
				cleanPins()
				controller()
				
			if timediff1 <= 2:
				keys.append(getKey())
				passiveBuzzer()
				bluePin()
				now3 = time.localtime() # get struct_time
				ts_digit3 = time.strftime("%H%M%S", now3)
				ts_list.append(3)
				timediff2 = int(ts_digit3) - int(ts_digit2)
				
			if timediff2 >= 2:
				redPin()
				longpassiveBuzzer()
				time.sleep(2)
				cleanPins()
				controller()
				
			if timediff2 <= 2:
				keys.append(getKey())
				passiveBuzzer()
				bluePin()
				now4 = time.localtime() # get struct_time
				ts_digit4 = time.strftime("%H%M%S", now4)
				ts_list.append(4)
				timediff3 = int(ts_digit4) - int(ts_digit3)
			
			if timediff3 >= 2:
				redPin()
				longpassiveBuzzer()
				time.sleep(2)
				cleanPins()
				controller()
			
			if timediff3 <= 2:
				data = str(keys)
				key_log = re.sub('[^0-9]+', '', data)
			if key_log[-len(code1):] == code1:
				#zway api command1
				os.system('/usr/bin/curl http://admin:pass@192.168.3.3:8083/ZAutomation/api/v1/devices/DummyDevice_26/command/on')
				greenPin()
				doublepassiveBuzzer()
				time.sleep(2)
				cleanPins()
				controller()

					
			elif key_log[-len(code2):] == code2:
				#zway api command2
				os.system('/usr/bin/curl http://admin:pass@192.168.3.3:8083/ZAutomation/api/v1/devices/Code_Device_toggleButton_18/command/on')
				greenPin()
				doublepassiveBuzzer()
				time.sleep(2)
				cleanPins()
				controller()
				

			elif key_log[-len(code3):] == code3:
				#zway api command3
				os.system('/usr/bin/curl http://admin:pass@192.168.3.3:8083/ZAutomation/api/v1/devices/Code_Device_toggleButton_22/command/on')
				greenPin()
				doublepassiveBuzzer()
				time.sleep(2)
				cleanPins()
				controller()
			
			elif (key_log[-len(code1):] != code1) and (key_log[-len(code2):] != code2) and (key_log[-len(code3):] != code3):
				redPin()
				longpassiveBuzzer()
				time.sleep(2)
				cleanPins()
				controller()
				
				


if __name__ == '__main__':

	init_irw()
	
	while True:
		controller()
			
		time.sleep(0.3)
