#!/usr/bin/python3

# import the necessary packages
from imutils.video import VideoStream
from pyzbar import pyzbar
import argparse
import datetime
import imutils
import time
from time import sleep
import cv2
import smtplib, re, os, sys
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


#FOR CSV/TXT file database, construct the argument parser and parse the arguments
ap = argparse.ArgumentParser()
#ap.add_argument("-o", "--output", type=str, default="database.csv", help="path to output CSV/TXT file containing barcodes")
ap.add_argument("-v", "--video", help="path to the video file")
ap.add_argument("-a", "--min-area", type=int, default=320, help="minimum area size") #for motion
args = vars(ap.parse_args())

# initialize the video stream and allow the camera sensor to warm up
#print("[INFO] starting video stream...")
if args.get("video", None) is None:
	vs = VideoStream(src=0).start()
	#vs = VideoStream(usePiCamera=True).start()
	time.sleep(2.0)
else:
	vs = cv2.VideoCapture(args["video"])
	
# open the output CSV/TXT file for writing and initialize the set of
# barcodes found thus far
#csv = open(args["output"], "w")
#found = set()
d = {'0053':'Courier', '0062':'Mom', '0082':'Son1', '0085':'Son2'}

#for motion
firstFrame = None

# loop over the frames from the video stream
while True:
	# grab the frame from the threaded video stream and resize it to
	# have a maximum width of 400 pixels
	frame = vs.read()
	frame = frame if args.get("video", None) is None else frame[1]
	
	if frame is None:
		break
	
	frame = imutils.resize(frame, width=320)
	# resize the frame, convert it to grayscale, and blur it
	gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
	gray = cv2.GaussianBlur(gray, (21, 21), 0)
 
	# if the first frame is None, initialize it
	if firstFrame is None:
		firstFrame = gray
		continue
	
	# compute the absolute difference between the current frame and first frame
	frameDelta = cv2.absdiff(firstFrame, gray)
	thresh = cv2.threshold(frameDelta, 50, 255, cv2.THRESH_BINARY)[1]
 
	# dilate the thresholded image to fill in holes, then find contours on thresholded image
	thresh = cv2.dilate(thresh, None, iterations=2)
	cnts = cv2.findContours(thresh.copy(), cv2.RETR_EXTERNAL,
		cv2.CHAIN_APPROX_SIMPLE)
	cnts = imutils.grab_contours(cnts)
	
	# loop over the contours
	for c in cnts:
		# if the contour is too small, ignore it
		if cv2.contourArea(c) < args["min_area"]:
			continue
			
		# compute the bounding box for the contour, draw it on the frame, and update the text
		#(x, y, w, h) = cv2.boundingRect(c)
		#cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 255, 255), 2)
		os.system('echo "0" > /sys/class/graphics/fb0/blank')
		
	# find the barcodes in the frame and decode each of the barcodes
	barcodes = pyzbar.decode(frame)
	# loop over the detected barcodes
	for barcode in barcodes:
		# extract the bounding box location of the barcode and draw
		# the bounding box surrounding the barcode on the image, change your color here
		(x, y, w, h) = barcode.rect
		cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
 
		# the barcode data is a bytes object so if we want to draw it
		# on our output image we need to convert it to a string first
		barcodeData = barcode.data.decode("utf-8")
		barcodeType = barcode.type
 
		# draw the barcode data and barcode type on the image, change your font size & color here
		text = "{} ({})".format(barcodeData, barcodeType)
		cv2.putText(frame, text, (x, y - 10),
			cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)
		
		'''# if the barcode text is currently not in our CSV file, write
		# the timestamp + barcode to disk and update the set
		if barcodeData not in found:
			csv.write("{},{}\n".format(datetime.datetime.now(),
				barcodeData))
			csv.flush()
			found.add(barcodeData)'''
		chiave = str(barcodeData)
		valore = ''
		for x in d.keys():
			valore=x
		# if the barcode text is currently in our CSV/TXT file do something
		if chiave in d.keys():
			os.system('gpio mode 0 out') #imposta il pin 0 come output usando la numerazione di wiringpi
			os.system('gpio write 0 1') #accendi/apri
			sleep(5)       
			os.system('gpio write 0 0') #spegni/chiudi
			#mail_content = 'Hello this is the attachment'    ###if you want an attachment
			#The mail addresses and password
			sender_address = 'sender@gmail.com'
			sender_pass = 'ofrgab2001'
			recipients = 'test@gmail.com, test1@gmail.com'
			#Setup the MIME
			message = MIMEMultipart()
			message['From'] = sender_address
			message['To'] = recipients
			message['Subject'] = 'ID ' + chiave + '-' + d[x] + ' ha imbucato i soldi'   #The subject line
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
	
	
	#add image to frame
	#img = cv2.imread('/home/pi/overlay.png')
	#img_height, img_width, _ = img.shape
	#frame[ 5:5+img_height , 5:5+img_width ] = img
	
	# show the output frame and set it fullscreen
	cv2.imshow("image2", frame)
	cv2.namedWindow("image2",cv2.WND_PROP_FULLSCREEN)
	cv2.setWindowProperty('image2', cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)
	key = cv2.waitKey(1) & 0xFF
 
	# if the `q` key was pressed, break from the loop
	if key == ord("q"):
		break
 
# close the output CSV file do a bit of cleanup
print("[INFO] cleaning up...")
csv.close()
cv2.destroyAllWindows()
vs.stop()
