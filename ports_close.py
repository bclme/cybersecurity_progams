import os

cmd = 'netstat -a -o -n > ports.txt'
os.system('cmd /c "'+ cmd + '"')
message=open(r'C:\backdoor\ports.txt', 'r')
lines =message.readlines()
message.close()
i=0
eports = '135 445 139'
pid = '4'
iport=[]
for line in lines:
   line = line.strip()
   if i>3:
     x = line.split(':')
     if line.find('[::]') != -1 and line.find('LISTENING') != -1:
        x = line.split(':')
        x[1]=x[3]
        x[2]=x[6]
     
     if x[2].find('LISTENING') != -1:
          y = x[1]          
          y = y[0:5]
          y = y.strip()
          
          z = x[2].split()
          a=z[-1]
          #print(a)
          if a != pid or eports.find(y) == -1:
             iport.append(y)
             os.system('taskkill /pid ' + a)
   i+=1 
iport = list(dict.fromkeys(iport))
for ports in iport:
   os.system('netsh advfirewall firewall add rule name="' + ports + 'port' + '" protocol=TCP dir=out remoteport=' + ports + ' action=block')
    
      
     

