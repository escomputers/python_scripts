#!/bin/python3

import os, sys, time, re
import imaplib, email, string

imap_host = 'smtp.gmail.com'
imap_user = 'test@gmail.com'
imap_pass = '1111111'

## open a connection 
imap = imaplib.IMAP4_SSL(imap_host)

## login
imap.login(imap_user, imap_pass)

## get status for unseen mail (folder) INBOX
folderStatus, UnseenInfo = imap.status('INBOX', "(UNSEEN)")
#print folderStatus


while True:
	#select specific folder
	status, data = imap.select('INBOX')
	#search unseen again
	typ, data = imap.search(None,'UnSeen')
	ids = data[0] # data is a list.
	id_list = ids.split() # ids is a space separated string
	try:
		latest_email_id = id_list[-1] # get the latest
		#get body
		typ, data = imap.fetch(latest_email_id, "(UID BODY[TEXT])")
		raw_email = data[0][1]
		msg = email.message_from_string(str(raw_email))
		messaggio = msg.get_payload(decode=True).splitlines()
		#STRING TO SEARCH INSIDE UNSEEN EMAILS
		my_str_as_bytes = str.encode('open')
		for line in messaggio:
			if my_str_as_bytes in line:
				#DO SOMETHING
				#os.system('gpio write 2 1')
	except:
		#os.system('gpio write 2 0')
		continue