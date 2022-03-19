import getpass
import telnetlib

HOST = "192.168.110.200"
user = input("Enter your username: ")
password = getpass.getpass()

tn = telnetlib.Telnet(HOST)

tn.read_until(b"Username: ")
tn.write(user.encode('ascii') + b"\n")
if password:
    tn.read_until(b"Password: ")
    tn.write(password.encode('ascii') + b"\n")

# Get into config mode
tn.write(b"conf t\n")

# Adds 5 vlans to the list with for loop
vlans = [101, 202, 303, 404, 505] # vlans to add in  a list
for i in vlans: # call (index) each item from list vlans
    command_1 = "vlan " + str(i) + "\n" # concatenate first command
    tn.write(command_1.encode('ascii')) # send command_1 with ASCII encoding
    command_2 = "name PYTHON_VLAN_" + str(i) + "\n" # concatenate second command
    tn.write(command_2.encode('ascii'))  # send command_2 with ASCII encoding

tn.write(b"end\n")
tn.write(b"exit\n")
print("exiting")
print(tn.read_all().decode('ascii')) 

