#!/bin/python3

#Threading, this will teach me how to thread, which means running multiple processes at once.
import sys
import socket
from datetime import datetime
from colorama import Fore, Style
import colorama

colorama.init()
#Define our target
if len(sys.argv) == 2:
    target = socket.gethostbyname(sys.argv[1]) #Translating host name to IPv4
else:
    print("["+ Style.BRIGHT + Fore.RED + "x"+ Style.RESET_ALL + "] Invalid amount of arguments.")
    print("["+ Style.BRIGHT + Fore.CYAN + "*" + Style.RESET_ALL +"] Syntax: Python3 Scanner.py <ip>")
    sys.exit(0)

def PortScan(HOST, scan_common):
    try:
        def GetProto(port):
            with open("common_ports", "r") as portlist:
                # Open port list from maalik, makes life easier
                ports = portlist.readlines()
                for line in ports:
                    if(str(port) in line):
                        return line

        def CheckPort(port):
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            socket.setdefaulttimeout(1)
            result = s.connect_ex((target,port)) #Returns an error indicator, moreover if a port is open the result back will be 0, if not open, its 1.
            if result == 0:
                return True
            s.close()
        
        def scan(port):
            if(CheckPort(port)):
                print("["+ Style.BRIGHT + Fore.GREEN + "+" + Style.RESET_ALL + "] {h}:{p} {proto}".format(h = HOST, p = port, proto = GetProto(port)))
        
        if(scan_common):
            with open("common_ports", "r") as portlist:
                # Open port list from maalik, makes life easier
                ports = portlist.readlines()
                for protoport in ports:
                    if("#" in protoport):
                        pass
                    else:
                        port = protoport.split(" ")[1].strip()
                        scan(int(port))
        else:
            try:
                rangess = input("["+ Style.BRIGHT + Fore.CYAN + "*" +  Style.RESET_ALL + "] Enter Range (eg: 0/255) : ")
                if("/" in rangess):
                    ports = rangess.split("/")
                    for port in range(int(ports[0]),int(ports[1])):
                        scan(port)
            except KeyboardInterrupt:
                print("["+ Style.BRIGHT + Fore.RED + "x"+ Style.RESET_ALL + "] Stopped.")
                sys.exit()
            except socket.gaierror:
                print("["+ Style.BRIGHT + Fore.RED + "x"+ Style.RESET_ALL + "] Hostname couldnot be resolved.")
                sys.exit()

            except socket.error:
                print("["+ Style.BRIGHT + Fore.RED + "x"+ Style.RESET_ALL + "] Could not connect to server!.")
                sys.exit()
    except Exception as e:
        print("["+ Style.BRIGHT + Fore.RED + "x"+ Style.RESET_ALL + "] Error : " + str(e))
    except KeyboardInterrupt:
        print("["+ Style.BRIGHT + Fore.RED + "x"+ Style.RESET_ALL + "] Stopped.")
        sys.exit()




#Add a pretty banner
# here added it for you
banner = Style.BRIGHT + Fore.GREEN +  r"""
 ▄▄▄·      ▄▄▄  ▄▄▄▄▄    .▄▄ ·  ▄▄·  ▄▄▄·  ▐ ▄  ▐ ▄ ▄▄▄ .▄▄▄  
▐█ ▄█▪     ▀▄ █·•██      ▐█ ▀. ▐█ ▌▪▐█ ▀█ •█▌▐█•█▌▐█▀▄.▀·▀▄ █·
 ██▀· ▄█▀▄ ▐▀▀▄  ▐█.▪    ▄▀▀▀█▄██ ▄▄▄█▀▀█ ▐█▐▐▌▐█▐▐▌▐▀▀▪▄▐▀▀▄ 
▐█▪·•▐█▌.▐▌▐█•█▌ ▐█▌·    ▐█▄▪▐█▐███▌▐█ ▪▐▌██▐█▌██▐█▌▐█▄▄▌▐█•█▌
.▀    ▀█▄▀▪.▀  ▀ ▀▀▀      ▀▀▀▀ ·▀▀▀  ▀  ▀ ▀▀ █▪▀▀ █▪ ▀▀▀ .▀  ▀
""" + Style.RESET_ALL

print(banner)

print("-" * 50)
print("Scanning Host " + target)
print("Time started:" + str(datetime.now()))
print("-" * 50)

mode = input("["+ Style.BRIGHT + Fore.GREEN + "+" + Style.RESET_ALL +"] Select Mode : \n[1] Scan for common Ports.\n[2] Enter Port Range.\n--> ")
if(mode == "1"):
    PortScan(target, True)
elif(mode == "2"):
    PortScan(target, False)
else:
    print("["+ Style.BRIGHT + Fore.RED + "x" + Style.RESET_ALL + "] Invalid Scan mode selected. Exiting.")
    sys.exit(0)
