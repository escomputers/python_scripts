from asterisk.ami import *
import time
from modules import call1

time.sleep(5)
#print("making second call..")

#chiama
client = AMIClient(address='',port=5038)
client.login(username='',secret='')

action = SimpleAction(
    'Originate',
    Channel='SIP/***************/**********', #per chiamate esterne usando un trunk
    Exten='2000',               #numero chiamante
    Priority=1,
    #Context='default',
    Context='from-internal',
    CallerID='Prova',
)

client.send_action(action)
time.sleep(10)
client.logoff()
