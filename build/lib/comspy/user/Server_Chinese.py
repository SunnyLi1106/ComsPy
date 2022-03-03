#!/usr/bin/python3
# 文件名：server.py

# 导入 socket、sys 模块
import socket
import sys
import threading

def server(Maximum_Number_Connections):
    # 创建 socket 对象
    serversocket = socket.socket(
                socket.AF_INET, socket.SOCK_STREAM)

    # 获取本地主机名
    host = socket.gethostname()

    port = int(input("请输入通信端口号(0~65535):"))

    # 绑定端口号
    serversocket.bind((host, port))

    # 设置最大连接数，超过后排队
    serversocket.listen(Maximum_Number_Connections)

    while True:
        # 建立客户端连接
        try:
            clientsocket,addr = serversocket.accept()      

            print("连接成功\n地址: %s" % str(addr))
            
            msg="连接成功\n地址: %s" % str(addr) + "\r"
            clientsocket.send(msg.encode('utf-8'))

            while True:
                msg = input("输入内容:") + "\r"
                clientsocket.send(msg.encode('utf-8'))
                if msg == "QUIT\r":
                    print("你中断了本次通信")
                    clientsocket.close()
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

def start(MaxNumCon=5):
    threading.Thread(target=server(MaxNumCon)).start()
