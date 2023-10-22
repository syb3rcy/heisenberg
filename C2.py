#!/usr/bin/python3

import socket
import json

def srvListener():
    ipAddr = '192.168.2.60'
    port = 1234

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    s.bind((ipAddr,port))
    s.listen(10)
    clientCon = ''
    while True:
        clientCon, clientAdd = s.accept()
        print(f"Connection from {clientAdd}")
        identity = clientCon.recv(1024).decode() #client will tell you who it is
        taskList = instructionSet(identity) # Checking to see if there's any tasks queue'd up for client
        taskList = json.dumps(taskList)
        
        clientCon.send(taskList.encode())
        reply = clientCon.recv(1024).decode()
        reply = json.loads(reply)
        dataStorage(identity, reply)
            
def instructionSet(identity):
    identity = 'Q' + str(identity) 
    try:
        fileRead = open('{}'.format(identity), 'r')      
    except:
        return ['Quit']
    return fileRead.readlines()

    
def dataStorage(identity, reply):     
    fileAppend = open('{}'.format(identity), 'a+')
    fileAppend.write(str(reply))
    #remove items from queue
    identity = 'Q' + str(identity) 
    f = open(identity, 'w')
    f.write('')   
    

if __name__=='__main__':
    srvListener()
