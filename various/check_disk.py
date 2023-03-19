#!/usr/bin/python3
import shutil
import socket
import os

# email packages
import smtplib
from email.mime.multipart import MIMEMultipart

usedTreshold = 50 # set treshold here #
sender_pass = os.getenv("GMAIL_PASS")

KB = 1024
MB = 1024 * KB
GB = 1024 * MB
hostname = socket.gethostname()

total = shutil.disk_usage('/').total
used = shutil.disk_usage('/').used
free = shutil.disk_usage('/').free

Usedpercentage = round(((100 * used) / total), 2)

if Usedpercentage > usedTreshold:
  #The mail addresses and password
  sender_address = 'emilianos13@gmail.com'
  recipients = 'emilianos13@gmail.com'
  #Setup the MIME
  message = MIMEMultipart()
  message['From'] = sender_address
  message['To'] = recipients
  message['Subject'] = 'Spazio su disco rimanente 20% su ' + hostname   #The subject line

  #Create SMTP session for sending the mail
  session = smtplib.SMTP('smtp.gmail.com', 587) 
  session.starttls() 
  session.login(sender_address, sender_pass) #login with mail_id and password
  text = message.as_string()
  session.sendmail(sender_address, recipients.split(','), text)
  session.quit()