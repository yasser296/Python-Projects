import getpass
import telnetlib

HOST = "10.1.1.1"
user = input("Enter your username: ")
password = getpass.getpass()

tn = telnetlib.Telnet(HOST)

tn.read_until(b"Username: ")
tn.write(user.encode('ascii') + b"\n")
if password:
    tn.read_until(b"Password: ")
    tn.write(password.encode('ascii') + b"\n")

tn.write(b"enable \n")
tn.write(b"123\n")
tn.write(b"config t \n")
tn.write(b"hostname Yasser \n")
tn.write(b"banner motd #Hello!# \n")

tn.write(b"interface s2/0 \n")
tn.write(b"no shutdown \n")
tn.write(b"ip address 10.1.2.10 255.255.255.0 \n")
tn.write(b"exit \n")

vlan_num = int(input("Enter The Number Of VLANs: "))

for i in range(2 , vlan_num):
    tn.write(b"vlan " + str(i).encode('ascii') + b"\n")
    tn.write(b"exit \n")

tn.write(b"exit \n")
# tn.write(b"write memory \n")



print("Done")
input("Just Press Enter!")

