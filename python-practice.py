#/bin/python3
import sys
import socket
from datetime import datetime

#define our target
if len (sys.argv) ==2: 
        target = socket.gethostbyname (sys.argv [1])
else: 
    print ("Invalid amount of arguments")

#add banner
print ("-" * 50)
print ("Scanning Target"+target)
print ("Time Started:" +str(datetime.now))
print ("-" * 50)

    


