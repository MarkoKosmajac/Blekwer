#imports
import socket
import os

#Variables
port = 0 #Add a Connection Port
lHost = "" #Add a Server IP or "0.0.0.0" for local

#Functions

def clear():
    os.system('cls' if os.name=='nt' else 'clear')

#Starting Server
serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = socket.gethostname()
serversocket.bind((host, port))
serversocket.listen(1) #allow only 1 connection

clear()
print("-:-:-:-:-:BLEKWER SERVER:-:-:-:-:-")
clientsocket, addr = serversocket.accept()
print("Incoming Connection from: " + str(addr))
while True:
    msg = input("Your Instruction: ")

    if msg == "help":
        clear()
        print("-+-+-+-+-+HELP+-+-+-+-+-")
        print("Test Connection: 'test'")
        
        input("\nPress ENTER to continue")
        clear()
        print("-:-:-:-:-:BLEKWER SERVER:-:-:-:-:-")
    
    elif msg == "exit" or msg == "stop":
        clear()
        print("-+-+-+-+-+EXITING BLEKWER SERVER+-+-+-+-+-")
        os._exit
        quit()
    
    else:
        msg = msg.encode("UTF-8")
        clientsocket.send(msg)
        msg = clientsocket.recv(4096)
        print(msg.decode("UTF-8"))