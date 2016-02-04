import socket
import time

UDP_IP = "169.254.0.9"
UDP_PORT = 5005

sock = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
sock.bind((UDP_IP,UDP_PORT))

while True:
	START = time.time()
	BR = 0.0
	BITS = 0.0

	data, addr = sock.recvfrom(1024)

	BITS += len(data) *8.0
	DUR = time.time() - START
	if DUR > 0.0:
		BR = (BITS/DUR)/1000000
	
	print "Received values:",data
	LEFTWHEEL,RIGHTWHEEL = data.split()
	print "Leftwheel recieved value:", LEFTWHEEL
	LFT2 = 2*int(LEFTWHEEL)
	print "Twice recieved leftwheel value:", LFT2
	print "Rightwheel recieved value:", RIGHTWHEEL
	RGT2 = 2*int(RIGHTWHEEL)
	print "Twice recieved rightwheel value :",RGT2
	print "Bitrate in Mbps:", BR
