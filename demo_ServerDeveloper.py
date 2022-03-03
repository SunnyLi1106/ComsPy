from comspy.developer import *

server_socket_init()
server_socket_bind(int(input("Enter a port:")))
server_setlisten(3)
server_buildconnect()
while True:
	msg = input("Enter a msg:")
	server_sendmsg(msg)
	if msg =="QUIT":
		exit()