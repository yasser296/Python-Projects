#!/usr/bin/python3 # shebang line to tell Linux to run this file as Python3 application

import os # import os module
import datetime # import datetime module

#with open closes file automatically, read the file from specified directory
with open("/root/py_nw_auto_scripts/chapter15_codes/ip_addresses.txt", "r") as ip_addresses: 
    print("-"*80) # Divider
    print(datetime.datetime.now()) # Print current time
    for ip_add in ip_addresses: # Use a simple for loop through each line in a file to get ip
        ip = ip_add.strip() # Remove any white spaces
        rep = os.system('ping -c 5 ' + ip) # Use Linux OS to send 5  ping (ICMP) messages
        if rep == 0: # response 0 means up
            print(f"{ip} is reachable.") # Informational
        else: # response is not 0, then there maybe network connectivity issue
            print(f"{ip} is either offline or icmp is filtered.") # Informational
            
print("-"*80,'\n') # Divider
print("All tasks completed.")
print('\n',"-"*80,'\n\n\n') # Divider
