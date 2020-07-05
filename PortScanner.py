#!/bin/python3

#Threading, this will teach me how to thread, which means running multiple processes at once.
import sys
import socket
from datetime import datetime

#Define our target
if len(sys.argv) == 2:
    target = socket.gethostbyname(sys.argv[1]) #Translating host name to IPv4
else:
    print("Invalid amount of arguments.")
    print("Syntax: Python3 Scanner.py <ip>")
#Add a pretty banner
print("-" * 50)
print("Scanning target" + target)
print("Time started:" + str(datetime.now()))
print("-" * 50)

try:
    for port in range(50,85):
        #print(port)
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        socket.setdefaulttimeout(1)
        result = s.connect_ex((target,port)) #Returns an error indicator, moreover if a port is open the result back will be 0, if not open, its 1.
        if result == 0:
            print("Port {} is open".format(port))
        s.close()

except KeyboardInterrupt:
    print("\nExiting Program")
    sys.exit()
except socket.gaierror:
    print("Hostname couldnot be resoloved.")
    sys.exit()

except socket.error:
    print("Coudld not connect to server!")
    sys.exit()
