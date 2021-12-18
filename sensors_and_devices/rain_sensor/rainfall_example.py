#!/usr/bin/python3

from gpiozero import Button


rain_sensor = Button(22)

#RAIN IN MM NEEDED TO ACTIVATE THE REED SWITCH
BUCKET_SIZE = 0.2794
count = 0

while True:
	def bucket_tipped():
		global count
		count += 1
		print(count)
		print (count * BUCKET_SIZE)
		
	def reset_rainfall():
		global count
		count = 0
		
	rain_sensor.when_pressed = bucket_tipped