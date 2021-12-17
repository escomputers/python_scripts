```
#REFERENCE
#http://denkovi.com/denkovi-relay-command-line-tool

#install java before

#before running any command, this commands below must be run
rmmod ftdi_sio
rmmod usbserial

#COMMANDS
#get all relay status
java -jar DenkoviRelayCommandLineTool.jar ID=0 8 all status

#get specific relay status
java -jar DenkoviRelayCommandLineTool.jar DAE06Lcq 8 7 status

#turn relay number 5 ON
java -jar DenkoviRelayCommandLineTool.jar ID=0 8 5 1

#turn relay number 5 OFF
java -jar DenkoviRelayCommandLineTool.jar ID=0 8 5 0
```