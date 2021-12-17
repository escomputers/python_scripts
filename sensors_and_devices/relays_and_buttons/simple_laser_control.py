#!/usr/bin/python3



from gpiozero import Button
from signal import pause

def sensore_innescato():
    print("Sensor activated")

def sensore_disinnescato():
    print("Sensor not  activated")

button = Button(16)

button.when_pressed = sensore_innescato
button.when_released = sensore_disinnescato

pause()
