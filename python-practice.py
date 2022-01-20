#/bin/python3
import sys
import socket
from datetime import datetime

#define our target
if len (sys.argv)
        target = socket.gethostbyname (sys.argv [1])
else: 
    print("Invalid amount of arguments")
    print(syntax: python3 scanner.py <ip>)
    

