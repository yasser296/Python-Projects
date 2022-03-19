#!/usr/bin/python3

import time
import paramiko
from getpass import getpass
# Custom tools
from precheck_tool import icmp_pinger

with open("/root/py_nw_auto_scripts/chapter15_codes/snmp_test/ip_addresses.txt" , "r") as ip_addresses:
    for ip in ip_addresses:
        ip = ip.strip()
        icmp_pinger(ip)

username = input("Enter username : ") # Ask for username
password = getpass("Enter password : " ) # Ask for password

with open("/root/py_nw_auto_scripts/chapter15_codes/snmp_test/ip_addresses.txt" , "r") as ip_addresses:
    for ip in ip_addresses:
        ip = ip.strip()
        eng_id = ip.replace(".", "") # Remove dot in ip address and use it as SNMP Engine ID
        print ("Now logging into " + (ip))
        ssh_client = paramiko.SSHClient()
        ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh_client.connect(hostname=ip,username=username,password=password)
        print (f"Successful connection to {ip}\n")
        print ("Now completing following tasks : " + "\n")
        remote_connection = ssh_client.invoke_shell()
        print (f"Adding SNMP configuration to {ip}")
        remote_connection.send("show clock\n")
        remote_connection.send("configure terminal\n") # Add SNMP configurations
        remote_connection.send(f"snmp-server engineID local {eng_id}\n")
        remote_connection.send("snmp-server group GROUP1 v3 priv\n")
        remote_connection.send("snmp-server user SNMPUser1 GROUP1 v3 auth sha AUTHPass1 priv aes 128 PRIVPass1\n")
        remote_connection.send("do write memory\n")
        remote_connection.send("exit\n")
        time.sleep(3)
        print ()
        time.sleep(3)
        output = remote_connection.recv(65535)
        print((output).decode('ascii'))
        print(f"Successfully configured {ip} & Disconnecting.")
        print("-"*80)
        ssh_client.close()
        time.sleep(3)

print("All tasks were completed successfully. Bye!")
