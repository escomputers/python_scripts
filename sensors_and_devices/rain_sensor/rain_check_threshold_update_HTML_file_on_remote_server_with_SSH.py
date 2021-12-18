#!/usr/bin/python3

from gpiozero import Button
import boto3, time, paramiko

#**************************************************************************************
#GPIO PIN NUMBER
rain_sensor = Button(22)

#MM OF RAIN TO ACTIVATE THE REED SWITCH
BUCKET_SIZE = 0.2794
count = 0
		
#THRESHOLD TO REACH IN 60SECONDS
trigger = 1

#START COUNTING TIME
start_time = time.time()

#hostname or IP address of the server containing the HTML file to be edited
ip_address = "ec2-1-1-1-1.eu-west-3.compute.amazonaws.com"

#**************************************************************************************
#CONNECT VIA SSH
def ssh_connect_with_retry(ssh, ip_address, retries):
			if retries > 3:
				return False
			privkey = paramiko.RSAKey.from_private_key_file(
				'linux-ami.pem')#SSH RSA private key .pem extension
			interval = 5
			try:
				retries += 1
				print('SSH into the instance: {}'.format(ip_address))
				ssh.connect(hostname=ip_address,
							username='root', pkey=privkey)
				return True
			except Exception as e:
				print(e)
				time.sleep(interval)
				print('Retrying SSH connection to {}'.format(ip_address))
				ssh_connect_with_retry(ssh, ip_address, retries)
				
#RAIN COUNT 
def conteggio_pioggia():
	global count
	count += 1
	qtapioggia = int(count * BUCKET_SIZE)
	#IF RAIN EXCEED THRESHOLD, WRITE 1 ON HTML SERVER FILE
	if qtapioggia >= trigger:
		ssh = paramiko.SSHClient()
		ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
		ssh_connect_with_retry(ssh, ip_address, 0)

		#WEB SERVER COMMANDS TO EXECUTE
		sftpclient = ssh.open_sftp()
		f = sftpclient.open("/var/www/html/rainfall.html", "wb")
		f.write("1")
		f.close()
		ssh.close()
		
		#WAIT 1 HOUR BEFORE CHECKIN AGAIN
		#time.sleep(3600)
			
#RESET RAIN COUNT
def reset_rainfall():
	global count
	count = 0

while True:
	def bucket_tipped():	
		reset_rainfall()
		
		#IF RAIN, CALL COUNT RAIN FUNCTION
		rain_sensor.when_pressed = conteggio_pioggia
		
		#IF NO RAIN OR THRESHOLD, WRITE 0 ON HTML SERVER FILE
		ssh = paramiko.SSHClient()
		ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
		ssh_connect_with_retry(ssh, ip_address, 0)

		#WEB SERVER COMMANDS TO EXECUTE
		sftpclient = ssh.open_sftp()
		f = sftpclient.open("/var/www/html/rainfall.html", "wb")
		f.write("0")
		f.close()
		ssh.close()
		
	#CALL RAIN COUNT FUNCTION EVERY MINUTE
	bucket_tipped()
	time.sleep(60.0 - ((time.time() - start_time) % 60.0))