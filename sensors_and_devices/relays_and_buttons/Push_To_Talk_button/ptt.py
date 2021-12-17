#!/bin/python



import RPi.GPIO as GPIO
import os

gpio_pin_number=21
#Replace YOUR_CHOSEN_GPIO_NUMBER_HERE with the GPIO pin number you wish to use
#Make sure you know which rapsberry pi revision you are using first
#The line should look something like this e.g. "gpio_pin_number=7"

GPIO.setmode(GPIO.BCM)
#Use BCM pin numbering (i.e. the GPIO number, not pin number)
#WARNING: this will change between Pi versions
#Check yours first and adjust accordingly

GPIO.setup(gpio_pin_number, GPIO.IN, pull_up_down=GPIO.PUD_UP)

program1 = 'xte \'keydown t\' '
program2 = 'xte \'keyup t\' '

try:
	while True:
		#GPIO.wait_for_edge(gpio_pin_number, GPIO.FALLING)
		if GPIO.input(gpio_pin_number) == 0:
			os.system(program1)
		else:
			os.system(program2)
except KeyboardInterrupt:  
    GPIO.cleanup()       # clean up GPIO on CTRL+C exit  
GPIO.cleanup()           # clean up GPIO on normal exit  			