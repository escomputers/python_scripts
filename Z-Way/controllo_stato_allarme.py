#!/bin/python3
import xml.etree.ElementTree as ET
import requests
import time
import json
import threading
import pytz
from datetime import datetime

alarmStartTime = datetime.strptime('21:30', '%H:%M')
alarmEndTime = datetime.strptime('8:30', '%H:%M')


def sensoreAperto():
    #WRITE THE STATUS CHANGE INTO XML FILE TO UPDATE VALUE ON ZWAY SERVER
    datafile = '/opt/z-way-server/htdocs/sensor1.xml'
    tree = ET.parse(datafile)
    root = tree.getroot()
    for child in root:
        #print(child.text)
        child.text = 'on'
    tree.write(datafile)


def sensoreChiuso():
    #WRITE THE STATUS CHANGE INTO XML FILE TO UPDATE VALUE ON ZWAY SERVER
    datafile = '/opt/z-way-server/htdocs/sensor1.xml'
    tree = ET.parse(datafile)
    root = tree.getroot()
    for child in root:
        #print(child.text)
        child.text = 'off'
    tree.write(datafile)


def controllo_stato_allarme():
    url = 'http://127.0.0.1:8083/ZAutomation/api/v1/devices/Security_17'
    r = requests.get(url)
    dict = json.loads(r.text)
    res = dict['data']['metrics']['state']
    last_state = (res.get('value'))
    if last_state == 0:
        on_url = 'http://localhost:8083/ZAutomation/api/v1/devices/DummyDevice_20/command/on'
        http_post = requests.get(on_url)


def main():
    threading.Timer(3.0, main).start()
    tmzone = pytz.timezone('Europe/Rome')
    now = (datetime.now(tmzone))

    start = now.replace(hour=alarmStartTime.hour, minute=alarmStartTime.minute)
    end = now.replace(hour=alarmStartTime.hour, minute=alarmStartTime.minute)

    if now >= start and now <= end:  # yes
        controllo_stato_allarme()


if __name__ == '__main__':
    main()