import paramiko # import paramiko library
import time # import time module
from datetime import datetime # import datetime module from datetime library

t_ref = datetime.now().strftime("%Y-%m-%d_%H-%M-%S") # Time reference in desired time format

file1 = open("routerslist") # open routerlist as file1

for line in file1: # for loop for router ip address
    print(t_ref) # print time reference
    print ("Now logging into " + (line)) # print statement
    ip_address = line.strip() # remove any white spaces

    file2= open("adminpass") # open adminpass as file2
    for line1 in file2: # read the first line(admin ID) in file 2
        username = line1.strip() # remove any white spaces
        for line2 in file2: # read the second line (password) in file2
            password = line2.strip() # remove any white spaces

            ssh_client = paramiko.SSHClient() # Create paramiko SSH client object 
            ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy()) # Automatically accept host key policy 
            ssh_client.connect(hostname=ip_address,username=username,password=password) # SSH connection objects
            print ("Successful connection to " + (ip_address) +"\n") # print statement
            print ("Now completing following tasks : " + "\n") # print statement 

            remote_connection = ssh_client.invoke_shell() # invoke shell session
            output1 = remote_connection.recv(3000) # Catches and removes the login prompt output
            # print(output1.decode('ascii')) # remove hash to print the login prompt message

            remote_connection.send("configure terminal\n") # Move to configuration mode
            print ("Configuring NTP Server") # print statement
            remote_connection.send("ntp server 192.168.110.133\n") # configure NTP server
            remote_connection.send("end\n") # go back to exec privilege mode
            remote_connection.send("write memory\n") # send save command
            print ("\n")

            time.sleep(2) 
            output2 = remote_connection.recv(65535) # capture session in output variable
            print((output2).decode('ascii')) # print output using ASCII decoding

            print (("Successfully configured your device & Disconnecting from ") + (ip_address)) # Print statement

            ssh_client.close() # Close SSH connection
            time.sleep(2) # Pause for 2 seconds

file1.close() # Close file1
file2.close() # Close file2
