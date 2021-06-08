#!/bin/python3

#Threading, this will teach me how to thread, which means running multiple processes at once.
import sys
import socket
import argparse
from datetime import datetime

def get_target_ports(string):
    if(string.isnumeric()):
        return int(string)
    elif("-" in string):
        r = string.split("-",1)
        return range(int(r[0]),int(r[1])+1)
    else:
        raise ValueError("Please input a valid port number (0 - 65535)")

def scan_port(ip, port):
    print("Scanning port:", str(port))
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    socket.setdefaulttimeout(1)

    result = s.connect_ex((target,port)) #Returns an error indicator, moreover if a port is open the result back will be 0, if not open, its 1.

    if result == 0:
        print("Port {} is open".format(port))
    s.close()

parser = argparse.ArgumentParser(prog='PortScanner v.1.0')
parser.add_argument("host", help="The target's hostname or ip-address")
parser.add_argument("-p", metavar="Port", help="The target port")
args = parser.parse_args()

try:
    target = socket.gethostbyname(args.host) #Translating host name to IPv4

    #Add a pretty banner
    print("-" * 50)
    print("Scanning target:", target)
    print("Time started:", str(datetime.now()))
    print("-" * 50)
    p = get_target_ports(args.p)
    if(isinstance(p, int)):
        scan_port(args.host,p)
    elif(isinstance(p,range)):
        for port in p:
            scan_port(args.host,port)

except KeyboardInterrupt:
    print("\nExiting Program")
    sys.exit()
except socket.gaierror:
    print("Hostname could not be resolved.")
    sys.exit()

except socket.error:
    print("Could not connect to server!")
    sys.exit()
