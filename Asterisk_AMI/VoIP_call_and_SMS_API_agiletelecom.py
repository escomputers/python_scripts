#!/bin/python3

from asterisk.ami import *
from urllib.request import urlopen
from urllib.parse import quote
import time

#invia sms
url = 'http://post.agiletelecom.com'
smsUSER = 'user'
smsPASSWORD = 'test'
smsNUMBER = '00393333333333;00393333333332'
smsSENDER = 'custom_sender'
smsTEXT = 'Alarm'
smsGATEWAY = 'H'
smsTYPE = 'file.sms'
smsDELIVERY = '20080601_A1'
http_req = url
http_req += '/smshurricane3.0.asp?'
http_req += "smsUSER="
http_req += quote(smsUSER)
http_req += "&smsPASSWORD="
http_req += quote(smsPASSWORD)
http_req += "&smsNUMBER="
http_req += quote(smsNUMBER)
http_req += "&smsSENDER="
http_req += quote(smsSENDER)
http_req += "&smsTEXT="
http_req += quote(smsTEXT)
http_req += "&smsGATEWAY="
http_req += quote(smsGATEWAY)
http_req += "&smsTYPE="
http_req += quote(smsTYPE)
http_req += "&smsDELIVERY="
http_req += quote(smsDELIVERY)
get = urlopen(http_req)
req = get.read()
get.close()

#WAIT FEW SECONDS BEFORE CALLING
#time.sleep(1)

#CALL
client = AMIClient(address='1.1.1.1',port=5038)
client.login(username='admin',secret='xxxxxxxxxxxxxxxxxxxxxxxxxxx')


action = SimpleAction(
    'Originate',
    Channel='SIP/Trunk01111111111/3333333333', #for external calls using a trunk
    Exten='2000',		#calling number (source)
    Priority=1,
    Context='default',
    CallerID='Alarm',
)

client.send_action(action)
