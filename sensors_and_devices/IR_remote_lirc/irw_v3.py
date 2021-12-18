#!/usr/bin/python3

import socket, re
from simplecrypto import encrypt


SOCKPATH = "/var/run/lirc/lircd"

sock = None

# Establish a socket connection to the lirc daemon
def init_irw():
	global sock
	sock = socket.socket(socket.AF_UNIX, socket.SOCK_STREAM)
	sock.connect(SOCKPATH)
	print ('Socket connection established!')
	print ('Ready...')

# parse the output from the daemon socket
def getKey():
	while True:
		data = sock.recv(128)
		data = data.strip()

		if (len(data) > 0):
			break

	words = data.split()
	clean_words = (words[2])
	a = (words[2]).decode()
	#return words[2], words[1]
	values = (a.split("_",1)[1])
	return values
	
# Main entry point
# The try/except structures allows the users to exit out of the program
# with Ctrl + C. Doing so will close the socket gracefully.
if __name__ == '__main__':
	try:
		init_irw()

		while True:
			#after 4 pressed digits encode string and prepare for API
			keys = []
			keys.append(getKey())
			keys.append(getKey())
			keys.append(getKey())
			keys.append(getKey())

			result = str(keys)
			clean_data = re.sub('[^0-9]+', '', result)
			
			'''#encrypt using AES-256
			password = "MJFJmsgxkC4v/T=7"
			msg = encrypt(clean_data,  password)'''

						
	except KeyboardInterrupt:
		print ("\nShutting down...")
		# Close the socket (if it exists)
		if (sock != None):
			sock.close()
		print ("Done!")