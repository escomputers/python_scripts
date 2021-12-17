#!/usr/bin/python3

#used sensor 
#240V 220V AC Alimentazione Sensore Opto-isolante Optoisolator Fotoaccoppiatore 5V 3.3V Arduino
#vcc pin sensor    --> shelly uni yellow pin   or --> +5V/+3.3V raspi
#out pin sensor    --> shelly uni white pin    or --> any GPIO pin raspi
#ground pin sensor --> shelly uni green pin    or --> ground pin raspi

#inside shelly uni web page configuration
#CHANNEL 1 -> ADC AUTOMATION -> ADC 1 ACTION over-adc thresold (mV): 2000 -> over-adc action: relay off
#CHANNEL 1 -> ADC AUTOMATION -> ADC 1 ACTION under-adc thresold (mV): 2000 -> under-adc action: relay on
#repeat for channel 2

from gpiozero import Button
from signal import pause

def rete_220V_OK():
    print("220V power restored")

def rete_220_KO():
    print("220V power outage")

button = Button(16)

button.when_pressed = rete_220V_OK
button.when_released = rete_220_KO

pause()
