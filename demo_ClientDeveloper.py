from comspy.developer import *

client_socket_init()
client_connect(int(input("Enter a port:")))
while True:
	msg = client_receivemsg(2048)
	if msg =="QUIT":
		exit()
	else:
		print(msg)