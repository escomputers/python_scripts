#!/usr/bin/python3

import time, os
import digitalio
import board
import adafruit_matrixkeypad
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
	
#WIRING
#https://learn.adafruit.com/matrix-keypad/pinouts



# Membrane 3x4 matrix keypad on Raspberry Pi -
# https://www.adafruit.com/product/419
#cols = [digitalio.DigitalInOut(x) for x in (board.D26, board.D20, board.D21)]
#rows = [digitalio.DigitalInOut(x) for x in (board.D5, board.D6, board.D13, board.D19)]
 
# 3x4 matrix keypad on Raspberry Pi -
# rows and columns are mixed up for https://www.adafruit.com/product/3845
cols = [digitalio.DigitalInOut(x) for x in (board.D13, board.D5, board.D26)]
rows = [digitalio.DigitalInOut(x) for x in (board.D6, board.D21, board.D20, board.D19)]
 
keys = ((1, 2, 3), (4, 5, 6), (7, 8, 9), ("*", 0, "#"))
 
keypad = adafruit_matrixkeypad.Matrix_Keypad(rows, cols, keys)

pin_codes_dict = ['2013', '2021', '8889']
codice1 = '2013'
codice2 = '2021'
codice3 = '8889'
key_log = ''
timestamps_log = ''

while True:
	keypressed = keypad.pressed_keys
	if keypressed:
		passiveBuzzer()
		bluePin()
		#print(keypressed)
		
		timestamps_list = []
		now = time.localtime() # get struct_time
		timestamp_digit = time.strftime("%H%M%S", now)
		timestamps_list.append(timestamp_digit)
		
		timestamps_log += (timestamps_list[0])
		key_log += str(keypressed[0])
	
		'''z = list(key_log)
		for i in z:
			times_pressed += 1'''

		#put a separator each 6 characters
		a = ','.join(timestamps_log[i:i+6] for i in range(0, len(timestamps_log), 6))
		
		#convert string into list made by items separated by delimiter (in this case comma)
		li = list(a.split(","))
		
		#convert each item in list into integer
		li_int = ([int(item) for item in li])
		
		#calculate difference between each consecutive item in list
		result_list = [t - s for s, t in zip(li_int, li_int[1:])]

		#get pin code lenght
		len_key_log = len(key_log)
		
		#create list with first element equal to zero
		list1 = [0]
		
		#concatenate two lists to avoid empty list errors
		list2 = list1 + result_list
		
		if (len_key_log == 4) and (key_log not in pin_codes_dict):
			redPin()
			longpassiveBuzzer()
			time.sleep(2)
			cleanPins()
			key_log = '' 				# clear keys log
			timestamps_log = '' 		# clear timestamps log
			
		#until entered pin code has the right lenght
		if len_key_log < 5:
			#if any value into the list is smaller than X seconds
			for i in lista2:
				if i > 6: #in this case 6 seconds
					#print("Error time exceeded")
					redPin()
					longpassiveBuzzer()
					time.sleep(2)
					cleanPins()
					key_log = '' 				# clear keys log
					timestamps_log = '' 		# clear timestamps log
				
				else:
					if key_log[-len(codice1):] == codice1:
						#zway api command1
						os.system('/usr/bin/curl http://admin:pass@192.168.3.3:8083/ZAutomation/api/v1/devices/DummyDevice_26/command/on')
						greenPin()
						doublepassiveBuzzer
						time.sleep(2)
						cleanPins()
						key_log = '' 			# clear keys log
						timestamps_log = '' 	# clear timestamps log

					if key_log[-len(codice2):] == codice2:
						#zway api command2
						os.system('/usr/bin/curl http://admin:pass@192.168.3.3:8083/ZAutomation/api/v1/devices/Code_Device_toggleButton_18/command/on')
						greenPin()
						doublepassiveBuzzer
						time.sleep(2)
						cleanPins()
						key_log = '' 			# clear keys log
						timestamps_log = '' 	# clear timestamps log
					
					if key_log[-len(codice3):] == codice3:
						#apri porta
						os.system('/usr/bin/curl http://admin:pass@192.168.3.3:8083/ZAutomation/api/v1/devices/Code_Device_toggleButton_22/command/on')
						greenPin()
						doublepassiveBuzzer()
						time.sleep(2)
						cleanPins()
						key_log = '' 			# clear keys log
						timestamps_log = '' 	# clear timestamps log

				
	time.sleep(0.3)