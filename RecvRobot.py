import socket
import numpy as np
import cv2
import sys
import time

UDP_IP = "Alpha.byod.gmu.edu"
UDP_PORT = 5006
BUFFER = 15872
sock = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
sock.bind((UDP_IP,UDP_PORT))

while True:
	#data,addr = sock.recvfrom(BUFFER),
	#print "Recieveing image: ", data.strip()
	file = open("Robot.jpeg",'wb')
	
	START = time.time()
	BR = 0.0
	BITS = 0.0
	
	data,addr = sock.recvfrom(BUFFER)
	
	BITS += len(data) *8.0
	DUR = time.time() - START
	if DUR > 0.0:
		BR = (BITS/DUR)/1000000
	
	
	while(data):
			file.write(data)
			sock.settimeout(5)
			data,addr = sock.recvfrom(BUFFER)
			datalength = len(data)
			if(datalength < BUFFER):
				break
		
        #data, addr = sock.recvfrom(1024)
        #Convert string to image data
        #imgdata = np.fromstring(data,np.uint8)
        #imgdata = open()
		#Reshape image data to proper size
        #img = np.reshape(imgdata,(200,200))
	
	print "Bitrate in Mbps:", BR
	image = cv2.imread('Robot.jpeg')
	cv2.imshow('image',image)
	cv2.waitKey(150)
