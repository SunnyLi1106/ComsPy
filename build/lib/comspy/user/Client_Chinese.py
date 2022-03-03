#!/usr/bin/python3

import socket
import sys
import time
import threading
from pyesytime import ALL_IN_ONE

def client(Message_Reception_Size):
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

	host = socket.gethostname()

	port = int(input("请输入通信端口号(0~65535):"))

	try:
		s.connect((host, port))
		while True:
			msg = s.recv(Message_Reception_Size)
			print(msg.decode('utf-8'))

			while True:
				msg = s.recv(Message_Reception_Size)
				if msg.decode('utf-8') != "\r":
					print("在"+ALL_IN_ONE()+"收到消息:\n"+msg.decode('utf-8'))
					if msg.decode('utf-8') == "QUIT\r":
						print("对方结束了本次通信")
						s.close()
						exit()
	except ConnectionResetError:
	    print("报出错误ConnectionResetError，可能是远程主机强制关闭现有连接")
	    exit()
	except ConnectionRefusedError:
	    print("报出错误ConnectionRefusedError，可能是目标计算机积极拒绝")
	    exit()
	except ConnectionAbortedError:
	    print("报出错误ConnectionAbortedError，可能是主机中的软件中止了一个已建立的连接")
	    exit()
	except BrokenPipeError:
	    print("报出错误BrokenPipeError")
	    exit()

def start(MsgRecSize=2048):
    threading.Thread(target=client(MsgRecSize)).start()
