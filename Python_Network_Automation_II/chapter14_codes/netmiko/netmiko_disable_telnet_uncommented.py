#!/usr/bin/env python3
import re
from netmiko import ConnectHandler
from getpass import getpass
import time
import  socket

def get_credentials():# Enhanced User ID and password collection tool
    #Prompts for, and returns a username and password
    global username # Make username as a global variable to be used throughout this script
    global password # Make password as a global variable to be used throughout this script
    username = input("Enter your username : ")
    password = None
    while not password:
        password = getpass()
        password_verify = getpass("Retype your password : ") # Verify the password is correctly typed
        if password != password_verify:
            print("Passwords do not match. Please try again.")
            password = None
    return username, password
get_credentials()    # Run this function first to collect the username and password


device1 = {                               # Netmiko dictionary for device1
'device_type': 'cisco_ios',
'ip': '192.168.183.10',
'username': username,
'password': password,
}
device2 = {                               # Netmiko dictionary for device2
'device_type': 'cisco_ios',
'ip': '192.168.183.20',
'username': username,
'password': password,
}
device3 = {                               # Netmiko dictionary for device3
'device_type': 'cisco_ios',
'ip': '192.168.183.101',
'username': username,
'password': password,
}
device4 = {                               # Netmiko dictionary for device4
'device_type': 'cisco_ios',
'ip': '192.168.183.102',
'username': username,
'password': password,
}
device5 = {                               # Netmiko dictionary for device5
'device_type': 'cisco_ios',
'ip': '192.168.183.133',
'username': username,
'password': password,
}

devices = [device1, device2, device3, device4, device5] # List of netmiko devices

for device in devices: # Loop through   devices
    ip = device.get("ip", "") # get value of the key "ip"
    for port in range (23, 24): # only port 23
        dest = (ip, port) # Combine ip and port number to form dest object
        try:
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock: # port scanner tool
                sock.settimeout(3) # add 3 seconds pause to socket application
                connection = sock.connect(dest) #
                print(f"On {ip}, port {port} is open!") # Informational
                net_connect = ConnectHandler(**device) # create a netmiko ConnectHandler object
                show_clock = net_connect.send_command("show clock\n") # Send "show clock" command
                print(show_clock) # Display time
                config_commands = ['line vty 0 15', 'transport input ssh'] # netmiko config_commands
                net_connect.send_config_set(config_commands) # send netmiko send_config_set
                output = net_connect.send_command("show run | b line vty") #send a show command to check vty 0 15
                print()# Informational
                print('-' * 80) # Displayed information separator line
                print(output) # Informational
                print('-' * 80) # Displayed information separator line
                print()# Informational
                net_connect.disconnect() # close netmiko connection

        except:
            print(f"On {ip}, port {port} is closed.")

            # # This is for saving the configuration after successful configuration change.
            net_connect = ConnectHandler(**device) # Commented out for third run
            write_mem = net_connect.send_command("write mem\n") # Commented out for third run
            print()
            print('-' * 80)
            print(write_mem) # Commented out for third run
            print('-' * 80)
            print()
            net_connect.disconnect()
