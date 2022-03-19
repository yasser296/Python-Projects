import getpass
import telnetlib

tn = telnetlib.Telnet("20.20.20.1")
tn.write(b"yasser\n")
tn.write(b"123\n")
tn.write(b"enable\n")
tn.write(b"123\n")
tn.write(b"config t \n")
tn.write(b"interface loopback 5 \n")
tn.write(b"ip address 5.5.5.5 255.255.255.255 \n")
tn.write(b"end \n")
tn.write(b"show ip inter br\n")
tn.write(b"wr me\n")
tn.write(b"exit \n")
print(tn.read_all().decode('ascii'))
