#!/usr/bin/python3

from time import sleep
import RPi.GPIO as GPIO

#GPIO.setmode(GPIO.BOARD)
GPIO.setmode(GPIO.BCM)
GPIO.setup(17, GPIO.OUT)
GPIO.output(17, 1) 
sleep(1)        
GPIO.output(17, 0)
GPIO.cleanup()