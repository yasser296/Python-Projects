#!/usr/bin/python3

import os

def icmp_pinger(ip):
    rep = os.system('ping -c 5 ' + ip)
    if rep == 0:
        print(f"{ip} is reachable.") # Print ip is reachable if the device is on the network
    else:
        print(f"{ip} is either offline or icmp is filtered. Exiting.")
        exit() # Exit application if any ip address is unreachable.
    print("-"*80)
