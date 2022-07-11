import sys
import os
import socket


def popper():
 print("")
 s.listen(1)
 print("")
 conn,addr = s.accept()
 while 1:
     
    command = input(str("Command >> "))
    conn.send(command.encode())
    files = conn.recv(5000)
    files = files.decode()
    print(files)
    
  

def poppee():
  while 1:
    
    
    files = s.recv(5000)
    files = files.decode()
    print(files)
    
    command = input(str("Command >> "))
    s.send(command.encode()) 
    
if __name__ == "__main__":
   s = socket.socket()
   port=sys.argv[2]
   print(sys.argv[1],sys.argv[2])
   if sys.argv[1] == '1':
     host=socket.gethostname()
     print(host)
     s.bind((host,int(port)))
     popper()
   else:
     host = sys.argv[3]
     print(host)
     s.connect((host,int(port)))
     poppee()    