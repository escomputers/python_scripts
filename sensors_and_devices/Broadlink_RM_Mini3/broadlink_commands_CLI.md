!#/usr/bin/python3

import os

os.system('')

./broadlink_discovery
./broadlink_cli --device "0x5f36 192.168.3.180 24dfa7deda9c" --learn
./broadlink_cli --device "0x5f36 192.168.3.180 24dfa7deda9c" --learnfile ac_off.power
./broadlink_cli --device "0x5f36 192.168.3.180 24dfa7deda9c" --learnfile ac_on_cool_16_highwind.power
./broadlink_cli --device "0x5f36 192.168.3.180 24dfa7deda9c" --send @ac_on_cool_16_highwind.power