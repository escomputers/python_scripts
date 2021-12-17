#!/usr/bin/python3

import bluetooth
import time, os

'''#generate a UUID
import subprocess
import sys, uuid
sys.stdout.write(uuid.uuid4().hex)'''

#bluetooth useful utility bluetoothctl

while True:
	result = bluetooth.lookup_name('XX:XX:XX:XX:XX:XX', timeout=5)
	if (result != None):
		#print("John: in")
		with open("/opt/z-way-server/automation/beacons/uuids.xml", "w") as f:
			f.write("9bb89cd5b1544648a429636fd00f13b0\n")
			f.close()
	else:
		#print("John: out")
		with open("/opt/z-way-server/automation/beacons/uuids.xml", "r") as f:
			lines = f.readlines()
		with open("/opt/z-way-server/automation/beacons/uuids.xml", "w") as f:
			for line in lines:
				if line.strip("\n") != "9bb89cd5b1544648a429636fd00f13b0":
					f.write(line)
					f.close()

	'''result = bluetooth.lookup_name('00:1D:D9:F9:79:43', timeout=5)
	if (result != None):
		#print("Paul: in")
		with open("/opt/z-way-server/automation/beacons/uuids.xml", "w") as f:
			f.write("bcc3b66179f145ada7ef0a612b06cd73\n")
			f.close()
	else:
		#print("Paul: out")
		with open("/opt/z-way-server/automation/beacons/uuids.xml", "r") as f:
			lines = f.readlines()
		with open("/opt/z-way-server/automation/beacons/uuids.xml", "w") as f:
			for line in lines:
				if line.strip("\n") != "bcc3b66179f145ada7ef0a612b06cd73":
					f.write(line)
					f.close()'''
	time.sleep(60)

