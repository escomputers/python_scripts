**Install and configure Mumble server**
```
apt-get install mumble-server
dpkg-reconfigure mumble-server
#or edit /etc/mumble-server.ini
```

**Install Mumble client on raspberry or android/iOS**
```
sudo apt-get install mumble
#edit /root/.config/Mumble/Mumble.conf

```
**Install xte to control system keyboard on raspberry**
```
sudo apt-get install xautomation
```
#Make a daemon or a cronjob for ptt.py