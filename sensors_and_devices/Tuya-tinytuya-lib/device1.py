#!/usr/bin/python3

import tinytuya

'''
DEVICES INFO all v.3.3
[
    {
        "name": "device1",
		"ip": "192.168.89.113",
        "id": "41444442840d8e97bdd5",
        "key": "8e0551d4e689a3ed"
    },
    {
        "name": "device2",
		"ip": "192.168.89.130",
        "id": "41444442840d8e9bd11f",
        "key": "199ac1a3cafdb853"
    },
    {
        "name": "device3",
		"ip": "192.168.89.129",
        "id": "41444442840d8e9bd719",
        "key": "9c9d54623f4cdc8f"
    },
    {
        "name": "device4",
		"ip": "192.168.89.112",
        "id": "41444442840d8e97bdcf",
        "key": "5cd189b1c2224cb7"
    }
]
'''

d = tinytuya.OutletDevice('41444442840d8e9bd11f', '192.168.89.109', '199ac1a3cafdb853')
d.set_version(3.3)
data = d.status() 

# Show status and state of first controlled switch on device
#print('Dictionary %r' % data)
#print('State (bool, true is ON) %r' % data['dps']['1'])  

# toggle switch state
switch_state = data['dps']['1']
data = d.set_status(not switch_state)  # This requires a valid key
'''if data:
	print('set_status() result %r' % data)'''