# file = open("E:\\python_projects\\Python_For_Networking_Course\\test.txt" , "w")


# id_num = input("Enter ID: ")
# ip = input("Enter IP: ")
# mask = input("Enter mask: ")

# file.write(f"router ospf 1\n\t router_id {id_num} \n\tip address {ip} {mask}")

# file.flush()
# file.close()



#########################################3
#############################################



file = open("E:/python_projects/Python_For_Networking_Course/test_2.txt" , "w")

ip = input("ip: ")
motd = input("motd: ")


file.write(f"""


	HOST = {ip}
	user = input("\\nEnter The Username: ")
	password = getpass.getpass()
	 
	tn = telnetlib.Telnet(HOST)
	
	tn.read_until(b"Username: ")
	tn.write(user.encode('ascii') + b"\\n")
	
	if password:
	    tn.read_until(b"Password: ")
	    tn.write(password.encode('ascii') + b"\\n")
	
	tn.write(b"enable \\n")
	tn.write(b"123\\n")
	tn.write(b"config t \\n")
	tn.write(b"hostname " + user.encode('ascii') + b"\\n")
	tn.write(b"banner motd #{motd}# \\n") 
	tn.write(b"interface " + str(port_num).encode('ascii') +  b"\\n")
	# tn.write(b"interface s2/0 \\n")
	tn.write(b"no shutdown \\n")
	tn.write(b"ip address 10.1.2.1 255.255.255.0 \\n")
	tn.write(b"exit \\n")

	""")

file.flush()
file.close()