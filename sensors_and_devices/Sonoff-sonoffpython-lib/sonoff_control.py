#!/bin/python3

import sonoff

config_username = 'youremail_used_to_register@gmail.com'
config_password = 'password'
config_api_region = 'eu'

s = sonoff.Sonoff(config_username, config_password, config_api_region)
devices = s.get_devices()
if devices:
	# We found a device, lets turn something on
	device_id = devices[0]['deviceid']
	print(device_id)
	#s.switch('on', device_id, None)

# update config
api_region = s.get_api_region
user_apikey = s.get_user_apikey
bearer_token = s.get_bearer_token