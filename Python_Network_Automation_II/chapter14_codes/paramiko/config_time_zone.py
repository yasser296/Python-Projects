import time
import paramiko


ip_addresses = ["192.168.110.140", "192.168.110.200", "192.168.110.201", "192.168.110.202", "192.168.110.203"]

username = "yasser"
password = "123"

ssh_client = paramiko.SSHClient()
ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
for ip in ip_addresses:
    ssh_client.connect(hostname = ip, username = username, password = password)
    print("Connected to " + ip + "\n")
    remote_connection = ssh_client.invoke_shell() # Create a shell for the session

    output1 = remote_connection.recv(3000) # Catches and removes the login prompt output
    print(output1.decode('ascii')) # remove hash to print the login prompt message
    print("\n")

    remote_connection.send("terminal length 0\n")
    remote_connection.send("configure terminal\n")
    remote_connection.send("clock timezone GMT +2\n") # Change to cairo timezone
    remote_connection.send("clock summer-time GMT recurring\n") # Change to your timezone summertime
    remote_connection.send("exit\n")

    time.sleep(2)
    
    remote_connection.send("clock set 15:15:00 12 feb 2022\n") # Change to current time
    remote_connection.send("write memory\n")
    remote_connection.send("end\n")

    output2 = remote_connection.recv(65535)  # save the remote_connection to variable
    print((output2).decode('ascii'))

    time.sleep(2)
    ssh_client.close()
    print("\n\n","-"*60,"\n\n\n\n\n")


