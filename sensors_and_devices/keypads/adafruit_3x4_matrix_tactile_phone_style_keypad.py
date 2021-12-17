#!/usr/bin/python3

import time, os
import digitalio
import board
import adafruit_matrixkeypad
from urllib.request import urlopen

#WIRING
'''
https://learn.adafruit.com/matrix-keypad/pinouts
'''


# 3x4 matrix keypad on Raspberry Pi -
# https://www.adafruit.com/product/419
#cols = [digitalio.DigitalInOut(x) for x in (board.D26, board.D20, board.D21)]
#rows = [digitalio.DigitalInOut(x) for x in (board.D5, board.D6, board.D13, board.D19)]
 
# 3x4 matrix keypad on Raspberry Pi -
# rows and columns are mixed up for https://www.adafruit.com/product/3845
cols = [digitalio.DigitalInOut(x) for x in (board.D13, board.D5, board.D26)]
rows = [digitalio.DigitalInOut(x) for x in (board.D6, board.D21, board.D20, board.D19)]
 
keys = ((1, 2, 3), (4, 5, 6), (7, 8, 9), ("*", 0, "#"))
 
keypad = adafruit_matrixkeypad.Matrix_Keypad(rows, cols, keys)

codice1 = '2013'
codice2 = '1111'
codice3 = '8889'
key_log = ''

while True:
	keypressed = keypad.pressed_keys
	if keypressed:
		os.system('aplay /root/beep.wav')
		key_log += str(keypressed[0])
		
		if key_log[-len(codice1):] == codice1:
			# make action1
			os.system('/usr/bin/python3 /root/open_door.py')
			os.system('/usr/bin/curl http://localhost:8083/ZAutomation/api/v1/devices/SecurityMode_27/command/off')
			key_log = '' # clear log

		if key_log[-len(codice2):] == codice2:
			# make action2
			os.system('/usr/bin/python3 /root/shelly_roller_control.py')
			key_log = '' # clear log
			
		if key_log[-len(codice3):] == codice3:
			# make action3
			os.system('/usr/bin/curl http://localhost:8083/ZAutomation/api/v1/devices/SecurityMode_27/command/on')
			key_log = '' # clear log
			
	time.sleep(0.3)
