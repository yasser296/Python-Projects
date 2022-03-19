import getpass
import telnetlib


HOSTS = ["192.168.110.200", "192.168.110.202"] # Create a list called HOSTS with two IPs
user = input("Enter your username: ")
password = getpass.getpass()

for HOST in HOSTS: # To loop through list, HOSTS
    print("SWITCH IP : " + HOST) # Marker to print out device IP
    tn = telnetlib.Telnet(HOST)

    tn.read_until(b"Username: ")
    tn.write(user.encode('ascii') + b"\n")
    if password:
        tn.read_until(b"Password: ")
        tn.write(password.encode('ascii') + b"\n")

    tn.write(b"conf t\n")
    for n in range (700, 800):
        tn.write(b"vlan " + str(n).encode('UTF-8') + b"\n") # you can use 'UTF-8' for numbers insted of 'ascii'
        tn.write(b"name PYTHON_VLAN_" + str(n).encode('UTF-8') + b"\n") 

    tn.write(b"end\n")
    tn.write(b"exit\n")

    print("\n\n")
    print(tn.read_all().decode('ascii'))

    print("\n\n\n\n\n\n")
