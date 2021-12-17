#!/bin/python
#compatibile anche con python3


from asterisk.ami import *

client = AMIClient(address='1.1.1.1',port=5038)
client.login(username='admin',secret='xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx')

#adapter = AMIClientAdapter(client)
action = SimpleAction(
	'Originate',
    #Channel='SIP/Trunk01111111111111/3333333333', #for external calls using a trunk
	Channel='SIP/6066', #number to call	(destination)
    Exten='6067',		#calling number (source)
    Priority=1,
    Context='default',
    CallerID='Alarm-House',
)
client.send_action(action)