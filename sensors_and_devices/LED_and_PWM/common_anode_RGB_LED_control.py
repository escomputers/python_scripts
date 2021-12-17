import time, os
import RPi.GPIO as GPIO
import threading, requests

'''
RGB LED COMMON ANODE CONNECTION
RED   PIN LED -> 220 Ohm resistor -> raspi PIN 11 (GPIO17)
GREEN PIN LED -> 220 Ohm resistor -> raspi PIN 12 (GPIO18 PCM_CLK)
BLUE  PIN LED -> 220 Ohm resistor -> raspi PIN 13 (GPIO27)
POSITIVE + PIN LED (LONGEST PIN)  -> any raspi 3V3 power PIN
'''

GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False) 

def redPin():
	#turn BLUE OFF
	GPIO.setup(13, GPIO.OUT)
	GPIO.output(13, 1)
	#turn GREEN OFF
	GPIO.setup(12, GPIO.OUT)
	GPIO.output(12, 1)
	#turn RED ON
	GPIO.setup(11, GPIO.OUT)
	'''p = GPIO.PWM(11, 50)  # channel=11 frequency=50Hz
	p.start(0)'''
	GPIO.output(11, 0)

def greenPin():
	#turn BLUE OFF
	GPIO.setup(13, GPIO.OUT)
	GPIO.output(13, 1)
	#turn RED OFF
	GPIO.setup(11, GPIO.OUT)
	GPIO.output(11, 1)
	#turn GREEN ON
	GPIO.setup(12, GPIO.OUT)
	GPIO.output(12, 0)
	
def bluePin():
	#turn GREEN OFF
	GPIO.setup(12, GPIO.OUT)
	GPIO.output(12, 1)
	#turn RED OFF
	GPIO.setup(11, GPIO.OUT)
	GPIO.output(11, 1)
	#turn BLUE ON
	GPIO.setup(13, GPIO.OUT)
	GPIO.output(13, 0)
	
def whitePin():
	#turn GREEN ON
	GPIO.setup(12, GPIO.OUT)
	GPIO.output(12, 0)
	#turn RED ON
	GPIO.setup(11, GPIO.OUT)
	GPIO.output(11, 0)
	#turn BLUE ON
	GPIO.setup(13, GPIO.OUT)
	GPIO.output(13, 0)
	
def controllo():
	try:
		threading.Timer(5.0, controllo).start()
		url = "https://www.google.it"
		r = requests.get(url, timeout=1)
		wanstate = os.popen('cat /sys/class/net/wan/carrier').read()
		wanstate_int = int(wanstate)
		if wanstate_int == 1:
			whitePin()
			#print("OK")
	except:
		redPin()
		#print("Internet KO/Network interface KO")

controllo()		