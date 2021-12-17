#!/usr/bin/python3

from time import sleep
import RPi.GPIO as GPIO
from keypad import keypad
import smtplib, re, os, sys
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText



def main():
	while True:
		#Initialize the keypad class.
		#Uncommont the matching initialzation to the imported package from above
		#Use the **optional** variable "columnCount" to change it from a 3x4 to a 4x4 keypad
		# kp = MCP230xx.keypad(address = 0x21, num_gpios = 8, columnCount = 4)
		kp = keypad(columnCount = 3)
		# kp = BBb_GPIO.keypad(columnCount = 3)

		GPIO.setup(13,GPIO.OUT)

		def digit():
			# Loop while waiting for a keypress
			r = None
			while r == None:
				r = kp.getKey()
			return r 
		 
		#print "Please enter a 4 digit code: "
		 
		# Getting digit 1, printing it, then sleep to allow the next digit press.
		d1 = digit()
		GPIO.output(13,1)
		sleep(1)
		#print d1
		GPIO.output(13, 0)
		sleep(1)
		 
		d2 = digit()
		GPIO.output(13,1)
		sleep(1)
		#print d2
		GPIO.output(13, 0)
		sleep(1)
		 
		d3 = digit()
		GPIO.output(13,1)
		sleep(1)
		#print d3
		GPIO.output(13, 0)
		sleep(2)
		 
		d4 = digit()
		GPIO.output(13,1)
		sleep(1)
		#print d4
		GPIO.output(13, 0)
		 
		# printing out the assembled 4 digit code.
		#print "You Entered %s%s%s%s "%(d1,d2,d3,d4)
		a = (d1,d2,d3,d4)
		b = str(a)
		c = re.sub('[^0-9]+', '', b) #togli le virgole
		d = {'0053':'user1', '0062':'user2', '0082':'user3'}
		if c in d.keys():
			#GPIO.setmode(GPIO.BCM)
			GPIO.setup(11, GPIO.OUT)
			GPIO.output(11, 1)         # set GPIO11 to 1/GPIO.HIGH/True  
			sleep(5)        
			GPIO.output(11, 0)
			GPIO.cleanup()
			#mail_content = 'Hello this is the attachment'    ###if you want an attachment
			#The mail addresses and password
			sender_address = 'sender@gmail.com'
			sender_pass = '111111'
			recipients = 'test@gmail.com, test1@gmail.com'
			#Setup the MIME
			message = MIMEMultipart()
			message['From'] = sender_address
			message['To'] = recipients
			message['Subject'] = d[c] + ' entered correct PIN'   #The subject line
			#if you want an attachment
			#message.attach(MIMEText(mail_content, 'plain'))
			
			#Create SMTP session for sending the mail
			session = smtplib.SMTP('smtp.gmail.com', 587) 
			session.starttls() 
			session.login(sender_address, sender_pass) #login with mail_id and password
			text = message.as_string()
			session.sendmail(sender_address, recipients.split(','), text)
			session.quit()
			#print('Mail Sent')
			#print("Key is present and value of the key is:")
			#print(d[c])
		else:
			#The mail addresses and password
			sender_address = 'sender@gmail.com'
			sender_pass = '11111111'
			recipients = 'test@gmail.com, test1@gmail.com'
			#Setup the MIME
			message = MIMEMultipart()
			message['From'] = sender_address
			message['To'] = recipients
			message['Subject'] = 'Wrong PIN'   #The subject line
			#if you want an attachment
			#message.attach(MIMEText(mail_content, 'plain'))
			
			#Create SMTP session for sending the mail
			session = smtplib.SMTP('smtp.gmail.com', 587) 
			session.starttls() 
			session.login(sender_address, sender_pass) #login with mail_id and password
			text = message.as_string()
			session.sendmail(sender_address, recipients.split(','), text)
			session.quit()
			#print("Key isn't present!")


