import socket
import sys
import time

UDP_IP = "Alpha.byod.gmu.edu"
UDP_PORT = 5006
BUFFER = 15872
IMAGE = "Robot.jpeg"
COUNT = 0

while(1):
	COUNT = COUNT + 1
	sock =socket. socket(socket.AF_INET,socket.SOCK_DGRAM)

	print "UDP target IP: ", UDP_IP
	print "UDP target port: ", UDP_PORT
	print "Sending image for the %s time." %COUNT
	file = open(IMAGE,"rb")
	data = file.read(BUFFER)

	print(len(data))
#	sock.sendto(IMAGE,(UDP_IP,UDP_PORT))
	sock.sendto(data,(UDP_IP,UDP_PORT))
	while (data):
		if(sock.sendto(data,(UDP_IP,UDP_PORT))):
			data = file.read(BUFFER)

	sock.close()
	file.close()
	time.sleep(0.2)



