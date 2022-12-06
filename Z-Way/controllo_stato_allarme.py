import os
import json
import requests
import threading
from datetime import datetime, timedelta


# imposta ora inizio
alarmStartTime = datetime.strptime('21:30', '%H:%M')


def allarme_on():
    url = 'http://127.0.0.1:8083/ZAutomation/api/v1/devices/Security_17'
    r = requests.get(url)
    dict = json.loads(r.text)
    res = dict['data']['metrics']['state']
    last_state = (res.get('value'))
    if last_state == 0:
        on_url = 'http://localhost:8083/ZAutomation/api/v1/devices/DummyDevice_20/command/on'
        http_on = requests.get(on_url)


def main():
    threading.Timer(3.0, main).start()

    # calcola orario di attivazione e disattivazione
    now = datetime.now()
    start = now.replace(hour=alarmStartTime.hour, minute=alarmStartTime.minute)
    end = (start + timedelta(hours=11))

    # se ci si trova nel periodo di accensione
    if now >= start and now <= end:

        # controlla l'ultimo reboot
        cmd_output = os.popen('uptime -s').read()

        # rimuovi spazi da stringa e converti a oggetto datetime
        cmd_output_cleaned = cmd_output.strip()
        last_reboot = datetime.strptime(cmd_output_cleaned, '%Y-%m-%d %H:%M:%S')

        # estrai ore e minuti da oggetto timedelta
        minutes_time_diff = ((now - last_reboot).seconds//60)%60

        # se sono passati più di due minuti dall'ultimo reboot
        if minutes_time_diff >= 2:
            allarme_on()


if __name__ == '__main__':
    main()
