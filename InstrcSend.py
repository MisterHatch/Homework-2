import socket

UDP_IP =  "169.254.0.9"
UDP_PORT = 5005
WHEELCONTROL = "3 7"

LEFTWHEEL,RIGHTWHEEL = WHEELCONTROL.split();

print "UDP target IP:", UDP_IP
print "UDP target port:", UDP_PORT
print "Left wheel instruction value:", LEFTWHEEL
print "Right wheel instruction value:", RIGHTWHEEL

sock = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
sock.sendto(WHEELCONTROL,(UDP_IP, UDP_PORT))
