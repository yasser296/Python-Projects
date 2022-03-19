import getpass
import telnetlib
import time  

user = input("Enter your username: ")
password = getpass.getpass()

file = open("/root/py_nw_auto_scripts/chapter13_codes/ip_addresses.txt") 

for ip in file: 
    print("Now configuring host IP : " + ip) 
    HOST = (ip.strip()) # Strips any white spaces
    tn = telnetlib.Telnet(HOST)

    tn.read_until(b"Username: ")
    tn.write(user.encode('ascii') + b"\n")
    if password:
        tn.read_until(b"Password: ")
        tn.write(password.encode('ascii') + b"\n")

    time.sleep(1) # Adds 1 second pause for device to respond
    # Configure a new user with privilege 3, allow show running-config 
    tn.write(b"conf t\n")
    tn.write(b"username junioradmin privilege 3 password 123\n")
    tn.write(b"privilege exec all level 3 show running-config\n") # Allow show running-config command
#    tn.write(b"file privilege 3\n") # give access to file, For routers only
    print("Added a new privilege 3 user") # Task ending statement

    tn.write(b"end\n")
    tn.write(b"exit\n")

    print("\n\n")
    print(tn.read_all().decode('ascii'))

    print("\n\n\n\n\n")
    
