#MAIN REFERENCE
#https://www.pyimagesearch.com/2018/05/21/an-opencv-barcode-and-qr-code-scanner-with-zbar/

```
#everything as ROOT
apt install python3-pip
apt install libzbar-dev
apt install libilmbase-dev libopenexr-dev libgstreamer1.0-dev
apt install libhdf5-dev libhdf5-serial-dev libhdf5-103
apt install libqtgui4 libqtwebkit4 libqt4-test python3-pyqt5
apt install libatlas-base-dev
apt install libjasper-dev
apt install libavcodec-dev libavformat-dev libswscale-dev libv4l-dev
pip3 install pyzbar
pip3 install imutils
pip3 install RPi.GPIO
apt install wiringpi
pip3 install opencv-contrib-python==4.1.0.25
```
-----------------------------------------------------------------------------------------------
#INSTALL RESISTIVE TOUCH DISPLAY 2.8" 320px**
https://learn.adafruit.com/adafruit-pitft-28-inch-resistive-touchscreen-display-raspberry-pi/easy-install-2
select yes at the 2nd question
-----------------------------------------------------------------------------------------------
```
#INSTALl OPENBOX TO DISPLAY WEBCAM VIDEO INTO A SEPARATE WINDOW
apt install xserver-xorg xinit openbox x11-xserver-utils**

#add to the bottom 
/etc/xdg/openbox/autostart

sudo python3 /path/script.py &
```
-----------------------------------------------------------------------------------------------
https://raspberrypi.stackexchange.com/questions/52099/using-openbox-to-autostart-gui-application-raspberry-pi-3
https://wiki.debian.org/it/Openbox (tty windows manager, no desktop)
https://wiki.debian.org/Screensaver
-----------------------------------------------------------------------------------------------
```
#screen blanking managed by X server, default 600s
#ssh with MobaXterm or similar program that allows X-11 forwarding

xhost + //disable access control list per X server
xset q   //print current settings timeout:600
xset s 300 //edit timeout e.g. 5min
xset s off //disable screen blanking
#in order to make changes permanent after reboot, add these commands at the end of /etc/xdg/openbox/autostart


#TURN DISPLAY ON
echo "0" > /sys/class/graphics/fb0/blank

#TURN DISPLAY OFF
echo "1" > /sys/class/graphics/fb0/blank

#DISPLAY USED PINS
Any 5V (Pin 2 or 4)
Any 3.3V (Pin 1 or 17)
Any Ground (Pin 6, 9, 14, 20, 25, 30, 34, or 39)
GPIO #18 (Pin 12) - Optional for backlight control
GPIO #24 (Pin 18)
GPIO #10/SPI MOSI (Pin 19)
GPIO #9/SPI MISO (Pin 21)
GPIO #25 (Pin 22)
GPIO #11/SPI CLK (Pin 23)
GPIO #8/SPI CE0 (Pin 24)
GPIO #7/SPI CE1 (Pin 26)
```
-----------------------------------------------------------------------------------------------
```
#INSTALL USB WIFI
sudo wget http://downloads.fars-robotics.net/wifi-drivers/install-wifi -O /usr/bin/install-wifi
sudo chmod +x /usr/bin/install-wifi
sudo install-wifi
nano /etc/wpa_supplicant/wpa_supplicant.conf
network={
    ssid="wifi"
    psk="1111"
}
```
-----------------------------------------------------------------------------------------------
```
#DISABLE MOUSE CURSOR INTO OPENBOX WINDOW
#mouse will move only when screen is touched

apt install unclutter
add to the bottom /etc/xdg/openbox/autostart
sudo unclutter -idle 0 &
```
-----------------------------------------------------------------------------------------------