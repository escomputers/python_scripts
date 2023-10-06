#!/usr/bin/python3

# import the necessary packages
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication


#The mail addresses and password
sender_address = 'emilianos13@gmail.com'
sender_pass = 'ipxhsmhiembjrynb'
recipients = 'emilianos13@gmail.com'
#Setup the MIME
message = MIMEMultipart()
message['From'] = sender_address
message['To'] = recipients
message['Subject'] = 'File inviato da te tramite SSH'   #The subject line

#if you want an attachment
attachmentPath = 'sec.zip'
try:
	with open(attachmentPath, "rb") as attachment:
		p = MIMEApplication(attachment.read(),_subtype="pdf")	
		p.add_header('Content-Disposition', "attachment; filename= %s" % attachmentPath.split("\\")[-1]) 
		message.attach(p)
except Exception as e:
	print(str(e))


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
		
