#!/usr/bin/python3

import socket
import sys
import threading

def server(Maximum_Number_Connections):

    serversocket = socket.socket(
                socket.AF_INET, socket.SOCK_STREAM)

    host = socket.gethostname()

    port = int(input("Please enter the communication port number(0~65535):"))

    serversocket.bind((host, port))

    serversocket.listen(Maximum_Number_Connections)

    while True:
        try:
            clientsocket,addr = serversocket.accept()      

            print("The connection is successful\nIn: %s" % str(addr))
            
            msg="The connection is successful\nIn: %s" % str(addr) + "\r"
            clientsocket.send(msg.encode('utf-8'))

            while True:
                msg = input("Enter the text:") + "\r"
                clientsocket.send(msg.encode('utf-8'))
                if msg == "QUIT\r":
                    print("You have interrupted this communication")
                    clientsocket.close()
                    exit()
        except ConnectionResetError:
            print("Error ConnectionResetError was reported, possibly because the remote host forced down an existing connection")
            exit()
        except ConnectionRefusedError:
            print("Error ConnectionRefusedError was reported, possibly because the target computer actively rejected it")
            exit()
        except ConnectionAbortedError:
            print("Error ConnectionAbortedError was reported, possibly because software on the host aborted an established connection")
            exit()
        except BrokenPipeError:
            print("BrokenPipeError was reported")
            exit()

def start(MaxNumCon=5):
    threading.Thread(target=server(MaxNumCon)).start()