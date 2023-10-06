import subprocess
import re
import math
import socket
import os

# email packages
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication

sender_address = 'emilianos13@gmail.com'
sender_pass = os.getenv('SENDER_PASS')
recipients = 'emilianos13@gmail.com'

command = "du -sh /home/Shinobi/exthdd"
disk_capacity = 458
used_treshold = 85 # set treshold here #

KB = 1024
MB = 1024 * KB
GB = 1024 * MB
hostname = socket.gethostname()

def sendMail():
    #Setup the MIME
    message = MIMEMultipart()
    message['From'] = sender_address
    message['To'] = recipients
    message['Subject'] = 'Spazio disco utilizzato ' + str(used_treshold) + '% su ' + hostname   #The subject line

    #Create SMTP session for sending the mail
    session = smtplib.SMTP('smtp.gmail.com', 587) 
    session.starttls() 
    session.login(sender_address, sender_pass) #login with mail_id and password
    text = message.as_string()
    session.sendmail(sender_address, recipients.split(','), text)
    session.quit()

# Run the command and capture its output
output = subprocess.check_output(command, shell=True, text=True)

disk_usage = int(re.search(r'\d+', output).group())

#free_space_percentage = ((disk_capacity - disk_usage) / disk_capacity) * 100
used_percentage = math.ceil((disk_usage / disk_capacity) * 100)

if used_percentage > used_treshold:
    sendMail()