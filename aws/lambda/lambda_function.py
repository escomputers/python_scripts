from asterisk.ami import *
import time

#chiama
client = AMIClient(address='13.38.90.239',port=5038)
client.login(username='admin',secret='6c62b5914cfc147d87f624ea3f3358b8')


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