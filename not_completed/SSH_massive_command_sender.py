#! /usr/bin/python3

import os
#import getpass
import paramiko
import csv
import socket
import re
import sys
import smtplib
from email import encoders
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email.mime.text import MIMEText


#username = input("Enter username for device login:")
username = "admin"

def enterMailPassword():
	while True: # repeat forever
		password = getpass.getpass("Enter SMTP password:")
		password_again = getpass.getpass("Confirm password:")
		if password != password_again:
			print("Password and confirmation do not match.Please try again!!")
		else:
			return password
def enterPassword():
	while True: # repeat forever
		password = getpass.getpass("Enter ssh devices password:")
		password_again = getpass.getpass("Confirm password:")
		if password != password_again:
			print("Password and confirmation do not match.Please try again!!")
		else:
			return password
#password = enterPassword()
password = "Fzf7WHvf"
#recipient = input("Enter your email-id where the results of the test will be mailed to you :")
recipient = "emilianos13@gmail.com"
#sender_address = input("Enter sender email address:")
sender_address = "service@arpanetitalia.com"
sender_pass = "arp$trSpd8889"
#sender_pass = enterMailPassword()
#subject = input("Enter subject for the mail:")
subject = "Risultati SSH Massive Command Sender"
#message = input("Enter the message body:")
message = "In allegato results.csv"
#SMTP_SERVER = input("Enter SMTP server FQDN:")
SMTP_SERVER = "mail.arpanetitalia.com"
SMTP_PORT = 587


# Opens file in read mode
f1 = open("hostfile","r")
f2 = open("commandfile","r")
# Creates list based on f1
devices = f1.readlines()
commands = f2.readlines()

ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

data = []
for device in devices:
	column = device.split()
	data.append([column[0]])
	for command in commands:
		try:
			conn=ssh.connect(column[0], username=username, password=password, timeout=4)
			if conn is None:
				stdin, stdout, stderr = ssh.exec_command(command)
				data[-1].append(stdout.read())
				ssh.close()
		except  paramiko.AuthenticationException:
			output = "Authentication Failed"
			data[-1].append(output)
			break
		except  paramiko.SSHException:
			output = "Issues with SSH service"
			data[-1].append(output)
			break
		except  socket.error:
			output = "Connection Error"
			data[-1].append(output)
			break
	data[-1] = tuple(data[-1])

f1.close()
f2.close()


'''#Create Workbook instance with xlsxwriter lib (not working)
book = xlsxwriter.Workbook("Workbook.xlsx")
sheet = book.add_worksheet("Sheet1")

#Define and format header
header_format = book.add_format({"bold":True , "bg_color":"yellow"})

for col, text in enumerate(header):
	sheet.write(0, col, text, header_format)
	
# Now, let"s write the contents
for row, data_in_row in enumerate(data):
	for col, text in enumerate(data_in_row):
		sheet.write(row + 1, col, text)

book.close()
'''

#Create csv instance
with open('results.csv', 'w') as f:
	fields = ['Indirizzo IP', 'Esito comando'] 
	file_writer = csv.writer(f)
	file_writer.writerow(fields)
	file_writer.writerows(data)
	

# Send excelsheet results in a mail
def main():
	msg = MIMEMultipart()
	msg["Subject"] = subject
	msg["To"] = recipient
	msg["From"] = sender_address
	part = MIMEText("text", "plain")
	part.set_payload(message)
	msg.attach(part)
	session = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
	session.starttls() 
	session.login(sender_address, sender_pass)
	fp = open("results.csv", "rb")
	msgq = MIMEBase("audio", "audio")
	msgq.set_payload(fp.read())
	fp.close()
	# Encode the payload using Base64
	encoders.encode_base64(msgq)
	# Set the filename parameter
	filename="results.csv"
	msgq.add_header("Content-Disposition", "attachment", filename=filename)
	msg.attach(msgq)
	# Now send or store the message
	datatxt = msg.as_string()
	session.sendmail(sender_address, recipient, datatxt)
	session.quit()


if __name__ == "__main__":
	main()