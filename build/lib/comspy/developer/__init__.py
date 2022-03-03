import socket
import sys

def server_socket_init():
	global serversocket
	serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

def server_socket_bind(port):
	global serversocket
	host = socket.gethostname()
	serversocket.bind((host, port))

def server_setlisten(num):
	global serversocket
	serversocket.listen(num)

def server_buildconnect():
	global serversocket,clientsocket
	clientsocket,addr = serversocket.accept()

def server_sendmsg(msg):
	clientsocket.send(msg.encode('utf-8'))

def client_socket_init():
	global clientsocket
	clientsocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

def client_connect(port):
	global clientsocket
	host = socket.gethostname()
	clientsocket.connect((host, port))

def client_receivemsg(size):
	global clientsocket
	msg = clientsocket.recv(size)
	return msg.decode('utf-8')