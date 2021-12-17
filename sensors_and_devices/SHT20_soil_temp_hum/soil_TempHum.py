#!/usr/bin/python3

from sensor import SHT20
from time import sleep
import threading



def soil_TempHum_sensing():
	threading.Timer(2.0, soil_TempHum_sensing).start()
	


	# I2C bus=1, Address=0x40
	sht = SHT20(1, 0x40)

	h = sht.humidity()  # read humidity
	#print(h)            # namedtuple
	#print(h.RH) 	# relative humidity

	t = sht.temperature()  # read temperature
	#print(t)               # namedtuple
	#print(t.C)             # Celsius


	
	#TEMPERATURA
	
	soil_temp = str(("%.2f" % round(t.C, 2)))
	#WRITE THE STATUS CHANGE INTO XML FILE TO UPDATE VALUE ON ZWAY SERVER
	with open('/opt/z-way-server/htdocs/soil_temp.html', 'w') as f:
		f.write(soil_temp)
		f.close()
		
	
	#UMIDITA'

	soil_hum = str(("%.2f" % round(h.RH, 2)))
	#WRITE THE STATUS CHANGE INTO XML FILE TO UPDATE VALUE ON ZWAY SERVER
	with open('/opt/z-way-server/htdocs/soil_humidity.html', 'w') as f:
		f.write(soil_hum)
		f.close()


soil_TempHum_sensing()
