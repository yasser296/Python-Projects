import getpass
import telnetlib

 
port_num = str(input("Enter the Number of Port and type: "))


HOST = "10.1.1.1"
user = input("\nEnter The Username: ")
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
tn.write(b"hostname " + user.encode('ascii') + b"\n")
tn.write(b"banner motd #Hello!# \n") 
tn.write(b"interface " + str(port_num).encode('ascii') +  b"\n")
# tn.write(b"interface s2/0 \n")
tn.write(b"no shutdown \n")
tn.write(b"ip address 10.1.2.1 255.255.255.0 \n")
tn.write(b"exit \n")


tn.write(b"exit \n") # To exit from Global Configration mode
tn.write(b"exit \n") # To exit from execuite mode so it will close the Session
tn.write(b"exit \n") # To exit from the terminal (cmd)

print("\nDone")
input("Just Press Enter To Exit!")
