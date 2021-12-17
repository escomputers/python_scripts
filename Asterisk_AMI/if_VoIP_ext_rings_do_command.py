#!/bin/python3
#This script was authored by AndrewH7 and belongs to him (www.instructables.com/member/AndrewH7)
#You have permission to modify and use this script only for your own personal usage
#You do not have permission to redistribute this script as your own work
#Use this script at your own risk

from asterisk.ami import AMIClientAdapter
from asterisk.ami import SimpleAction
from asterisk.ami import AMIClient
from asterisk.ami import EventListener
import os, sys, time, re

client = AMIClient(address='1.1.1.1',port=5038)
client.login(username='admin',secret='XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX')

while True:
	action = SimpleAction(
	'ExtensionState',
	Exten='6067',		
	Context='default'
	)
	
	future = client.send_action(action)
	data = str(future.response)

	if 'Ringing' in data:
		#DO SOMETHING
	else:
		continue