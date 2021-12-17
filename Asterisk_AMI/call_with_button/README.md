- raspbian 10 buster desktop
- USB speakers with mic
- chmod 755 for each file

AVAILABLE LIBS
https://wiki.asterisk.org/wiki/display/AST/AMI+Libraries+and+Frameworks

CHOOSEN LIB
https://pypi.org/project/asterisk-ami/
Control ACL e general config into /etc/asterisk/manager.conf

GPIO LIB
https://pypi.org/project/RPi.GPIO/
-----------------------------------------------------------------------------------------------
#PIN NEEDED TO CONNECT A BUTTON
positive = any gpio pin
negative = ground
-----------------------------------------------------------------------------------------------
#CLIENT SIP TWINKLE
https://github.com/LubosD/twinkle

```
apt install ucommon-utils libccrtp-dev libzrtpcpp-dev libsndfile-dev libmagic-dev libreadline-dev cmake flex bison libasound-dev qt5-default qttools5-dev qtdeclarative5-dev qml-module-qtquick-controls libxml2 libxml2-dev
git clone https://github.com/LubosD/twinkle.git
cd twinkle
mkdir build && cd build
sudo cmake ..
sudo make
make install


#CONFIG FILES
nano /root/.twinkle/twinkle.cfg
nano /root/.twinkle/twinkle.svc #ENABLE AUTO-ANSWER HERE
nano /root/.twinkle/twinkle.sys #SPEAKERS AND MIC CONFIG
```
-----------------------------------------------------------------------------------------------
```
#SYSTEMD SERVICE FOR CALL BUTTON
nano /etc/systemd/system/callbutton.service

[Unit]
Description=pulsante service
After=network.target 

[Service]
ExecStart=/usr/bin/python3 /home/pi/pulsantechiamata.py
Restart=on-failure

[Install]
WantedBy=multi-user.target
Alias=pulsante.service


systemctl daemon-reload
systemctl start pulsante.service
systemctl enable pulsante.service
```
-----------------------------------------------------------------------------------------------
#START TWINKLE INTO OPENBOX WINDOW AT START TIME
```
add to the bottom /etc/xdg/openbox/autostart
sudo twinkle &
```
-----------------------------------------------------------------------------------------------
