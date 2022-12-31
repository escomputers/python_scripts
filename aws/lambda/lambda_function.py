from asterisk.ami import *
import time

#chiama
client = AMIClient(address='13.38.90.239',port=5038)
client.login(username='admin',secret='')


action = SimpleAction(
    'Originate',
    Channel='SIP/Messagenet09321846766/3936926490', #per chiamate esterne usando un trunk
    Exten='3000',               #numero chiamante
    Priority=1,
    #Context='default',
    Context='from-internal',
    CallerID='Allarme-Ufficio',
)

client.send_action(action)
time.sleep(10)
client.logoff()
