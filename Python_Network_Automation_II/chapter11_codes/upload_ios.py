import getpass
import telnetlib

HOST = "192.168.110.140"
user = input("Enter your telnet username: ")
password = getpass.getpass()

tn = telnetlib.Telnet(HOST)

tn.read_until(b"Username: ")
tn.write(user.encode('ascii') + b"\n")
if password:
    tn.read_until(b"Password: ")
    tn.write(password.encode('ascii') + b"\n")

tn.write(b"enable\n")
tn.write(b"123\n")
tn.write(b" copy tftp://192.168.110.132/c2691-entservicesk9-mz.124-13b.bin flash:c2691-entservicesk9-mz.124-13b.bin\n")  
tn.write(b"\n")
tn.write(b"\n")    
tn.write(b"exit\n") 

print(tn.read_all().decode('ascii'))
