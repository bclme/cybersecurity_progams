#coding:utf-8
import os
import sys
 
import time
from datetime import datetime
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
os.system("color")
class Handler(FileSystemEventHandler):
   
    @staticmethod
    def on_any_event(event):
        if event.is_directory:
            return None
  
        elif event.event_type == 'created':
            # Event is created, you can process it now
            print("Watchdog received created event - % s." % event.src_path)
            print("\r", end="", flush=True)
        elif event.event_type == 'modified':
            # Event is modified, you can process it now
            print("Watchdog received modified event - % s." % event.src_path)
            print("\r", end="", flush=True)
    exit
watchDirectory = '.'
observer = Observer()
event_handler = Handler()
observer.schedule(event_handler, watchDirectory, recursive = True)
observer.start()

while True:
    
    now = datetime.now()
    print ("%s/%s/%s %s:%s:%s" % (now.month,now.day,now.year,now.hour,now.minute,now.second)) 
    print("\r", end="", flush=True)
    Usb = os.popen("wmic logicaldisk where drivetype=2 get description ,deviceid ,volumename").read()
    print(Usb)
    if Usb.find("DeviceID") != -1:
        print("Usb is plugged")
        #input("")
        print("\r", end="", flush=True)

    else:
        print("Usb is not plugged")
        #input("")
        print("\r", end="", flush=True)
    time.sleep(1)
 
 
