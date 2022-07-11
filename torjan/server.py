import os
import socket

x = socket.socket()
host='DESKTOP-IMR6DAM'#my pc name
port=4040
x.bind((host,port))
print("")
x.listen(1)
conn,addr = x.accept()
print("")


while 1:
  command = input(str("Command >> "))#enter command
  if command == "dir":
    conn.send(command.encode())
    print("")
    files = conn.recv(5000)
    files = files.decode()
    print("Command output: " , files)
  elif command == "files":
    conn.send(command.encode())
    user_input = input(str("Folder: "))
    conn.send(user_input.encode())
    print(" ")
    files = conn.recv(5000)
    files = files.decode()
    print("Files(List Format): " , files)
  elif command == "copyfile":
    conn.send(command.encode())
    filepath= input(str("Filename: "))
    conn.send(filepath.encode())
    print("")
    files = conn.recv(100000)  
    filename= input(str("Filename: "))    
    new_file=open(filename, "wb")
    new_file.write(files)
    print("")
    new_file.close()
  elif command == "delfile":
    conn.send(command.encode())
    filepath = input(str("Filename: "))
    conn.send(filepath.encode())
    print("")
  elif command == "uplfile":
    conn.send(command.encode())
    filepath = input(str("Filename to be uploaded: "))
     
    file = open(filepath,"rb")
    data = file.read()
    conn.send(data)
    print("")
    
  else:
    print("Invalid Command")
  