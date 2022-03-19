import getpass
import telnetlib

HOST = "192.168.110.202" # Update this to lab-sw2 switch IP
user = input("Enter your username: ")
password = getpass.getpass()

tn = telnetlib.Telnet(HOST)

tn.read_until(b"Username: ")
tn.write(user.encode('ascii') + b"\n")
if password:
    tn.read_until(b"Password: ")
    tn.write(password.encode('ascii') + b"\n")

# Get into to config mode
tn.write(b"conf t\n")

# Add 5 random vlans to vlans list and use  while loop to configure them to the switch
vlans = [101, 202, 303, 404, 505] # vlans to add in list
i = 0 # initial index value
while i < len(vlans): # while i is smaller than the length of vlans
    print(vlans[i]) # print vlans item
    command_1 = "vlan " + str(vlans[i]) + "\n" # concatenate first command
    tn.write(command_1.encode('ascii')) # send command_1 with ASCII encoding
    command_2 = "name PYTHON_VLAN_" + str(vlans[i]) + "\n" # concatenate second command
    tn.write(command_2.encode('ascii')) # send command_2 with ASCII encoding
    i +=1 

tn.write(b"end\n")
tn.write(b"exit\n")
print("exiting")
print(tn.read_all().decode('ascii'))
