import RPi.GPIO as GPIO
import time, os
import random
 
#pins 
#R = 11, G = 12, B = 13
 
def setup():
	global pwmR, pwmG, pwmB
	GPIO.setwarnings(False)
	GPIO.setmode(GPIO.BOARD)
	GPIO.setup(11, GPIO.OUT)
	GPIO.output(11, 1)
	GPIO.setup(12, GPIO.OUT)
	GPIO.output(12, 1)
	GPIO.setup(13, GPIO.OUT)
	GPIO.output(13, 1)
	pwmR = GPIO.PWM(11, 2000)  # set each PWM pin to 2 KHz
	pwmG = GPIO.PWM(12, 2000)
	pwmB = GPIO.PWM(13, 2000)
	pwmR.start(0)   # initially set to 0 duty cycle
	pwmG.start(0)
	pwmB.start(0)
	 
def setColor(r, g, b):  # 0 ~ 100 values since 0 ~ 100 only for duty cycle
	pwmR.ChangeDutyCycle(r)
	pwmG.ChangeDutyCycle(g)
	pwmB.ChangeDutyCycle(b)
	 
def displayColors():
	setColor(100, 0, 0) #   red color
	time.sleep(1)   # 1s
	setColor(0, 100, 0) # green
	time.sleep(1)   # 1s
	setColor(0, 0, 100) # blue
	time.sleep(1)   # 1s
	setColor(100, 100, 0) # yellow
	time.sleep(1)   # 1s
	setColor(0, 100, 100) # cyan
	time.sleep(1)   # 1s
	setColor(100, 0, 100) # magenta
	time.sleep(1)   # 1s
	setColor(50, 0, 0) # maroon
	time.sleep(1)   # 1s
	setColor(50, 0, 50) # purple
	time.sleep(1)   # 1s
	setColor(0, 0, 50) # navy
	time.sleep(1)   # 1s

def displayGreen():
	setColor(0, 100, 0) # green
	time.sleep(1)   # 1s
	
def displayRed():
	setColor(0, 100, 0) # green
	time.sleep(1)   # 1s
	
def destroy():
	pwmR.stop()
	pwmG.stop()
	pwmB.stop()
	#turn off the led after cycle
	GPIO.cleanup()
	
	
setup()
displayColors()
destroy()
