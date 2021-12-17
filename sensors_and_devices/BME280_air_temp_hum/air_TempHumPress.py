#!/usr/bin/python3

#import smbus2
#import bme280
import threading

import board
from adafruit_bme280 import basic as adafruit_bme280 
i2c = board.I2C() 
bme280 = adafruit_bme280.Adafruit_BME280_I2C(i2c)
#port = 1 
#address = 0x77
#bus = smbus2.SMBus(port)
#calibration_params = bme280.load_calibration_params(bus, address)

	
def air_TempHumPress_sensing():
	#port = 1
	#address = 0x77
	#bus = smbus2.SMBus(port)
	#calibration_params = bme280.load_calibration_params(bus, address)
	#data = bme280.sample(bus, address, calibration_params)
	threading.Timer(10.0, air_TempHumPress_sensing).start()
	#data = bme280.sample(bus, address, calibration_params)
	
	'''# the sample method will take a single reading and return a
	# compensated_reading object

	#the compensated_reading class has the following attributes
	print(data.id)
	print(data.timestamp)
	print(data.temperature)
	print(type(data.temperature))
	print()
	print(data.pressure)
	print(type(data.pressure))
	print()
	print(data.humidity)
	print(type(data.humidity))
	print()
	#there is a handy string representation too
	#print(data)'''
	
	'''
	TEMPERATURE
	'''
	air_temp = str(("%.2f" % round(bme280.temperature, 2)))
	#WRITE THE STATUS CHANGE INTO XML FILE TO UPDATE VALUE ON ZWAY SERVER
	with open('/opt/z-way-server/htdocs/air_temp.html', 'w') as f:
		f.write(air_temp)
		f.close()
		
	'''
	HUMIDITY
	'''
	air_hum = str(("%.2f" % round(bme280.humidity, 2)))
	#WRITE THE STATUS CHANGE INTO XML FILE TO UPDATE VALUE ON ZWAY SERVER
	with open('/opt/z-way-server/htdocs/air_humidity.html', 'w') as f:
		f.write(air_hum)
		f.close()

	'''
	AIR PRESSURE
	'''
	air_press = str(("%.2f" % round(bme280.pressure, 2)))
	#WRITE THE STATUS CHANGE INTO XML FILE TO UPDATE VALUE ON ZWAY SERVER
	with open('/opt/z-way-server/htdocs/air_pressure.html', 'w') as f:
		f.write(air_press)
		f.close()


air_TempHumPress_sensing()
