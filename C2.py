#!/usr/bin/python3

import socket
import threading
import time
responses = {}

def srvListener():
    ipAddr = '192.168.2.58'
    port = 1234
    msgSrv = "pwd"

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    s.bind((ipAddr,port))
    s.listen(10)
    clientCon = ''
    while True:
        clientCon, clientAdd = s.accept()
        print(f"Connection from {clientAdd}")
       
        clientCon.send(msgSrv.encode())
        msg = clientCon.recv(1024).decode()
        if msg:
            storage(msg)

def storage(info):
    global responses
    info = info.split(":") 
    responses[info[0]] = info[1]
    output()

def output():
    print(responses)
    print(type(responses))  

if __name__=='__main__':
    t1= threading.Thread(target=srvListener)
    t1.start()
