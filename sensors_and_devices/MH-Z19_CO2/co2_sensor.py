#!/usr/bin/python3

import mh_z19
import threading, re

def co2_sensing():
	threading.Timer(2.0, co2_sensing).start()
	valore = mh_z19.read()
	res = str(valore)
	#remove co2 word from result
	res1 = res.replace("co2", "")
	#regex to match a string of characters that are not a letters or numbers
	res2 = re.sub('[^A-Za-z0-9]+', '', res1)
	#WRITE THE STATUS CHANGE INTO XML FILE TO UPDATE VALUE ON ZWAY SERVER
	with open('/opt/z-way-server/htdocs/co2.xml', 'w') as f:
		f.write('<item><value>' + res2 + '</value></item>')
		f.close()
	
co2_sensing()
