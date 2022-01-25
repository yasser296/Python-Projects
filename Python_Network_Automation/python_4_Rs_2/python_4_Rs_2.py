import getpass
import telnetlib


Rs_num = int(input("Enter the Number of Routers: "))

for i in range(1 , Rs_num + 1):
    HOST = f"10.1.1.{i}"
    print("\nHost IP: " + HOST)
    user = input("\nEnter The Username of " + "R" + str(i) + " : ")
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
    # tn.write(b"hostname Yasser \n")
    tn.write(b"banner motd #Hello!# \n")

    tn.write(b"interface s2/0 \n")
    tn.write(b"no shutdown \n")
    tn.write(b"ip address 10.1.2." + str(i).encode('ascii') + b" 255.255.255.0 \n")
    # tn.write(b"ip address 10.1.2.10 255.255.255.0 \n")
    tn.write(b"exit \n")

    tn.write(b"interface loopback " + str(i).encode('ascii') +  b"\n")
    tn.write(b"no shutdown \n")
    tn.write(b"ip address " + str(i).encode('ascii') + b"." + str(i).encode('ascii') +  b"." + str(i).encode('ascii') + b"." + str(i).encode('ascii') + b" 255.255.255.0 \n")
    tn.write(b"exit \n")


    tn.write(b"exit \n") # To exit from Global Configration mode
    tn.write(b"exit \n") # To exit from execuite mode so it will close the Session
    tn.write(b"exit \n") # To exit from the terminal (cmd)


    print("\nR" + str(i) + " is Done")
    input("\nPress Enter To Contiue.")


print("\nAll Routers Are Done")
input("Just Press Enter To Exit!")

