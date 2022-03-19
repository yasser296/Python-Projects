import time
import paramiko

ip_addresses = ["192.168.110.140", "192.168.110.200", "192.168.110.201", "192.168.110.202", "192.168.110.203"]

username = "yasser"
password = "123"

ssh_client = paramiko.SSHClient()
ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

for ip in ip_addresses:
    ssh_client.connect(hostname=ip, username=username, password=password)
    print("Connected to " + ip + "\n")
    remote_connection = ssh_client.invoke_shell()
    output1 = remote_connection.recv(3000) # Catches and removes the login prompt output
    # print(output1.decode('ascii')) # remove hash to print the login prompt message
    # Now send the commands you want to run and display on the screen
    remote_connection.send("show ntp status\n")
    remote_connection.send("show run | in ntp\n")
    time.sleep(2)
    output2 = remote_connection.recv(6000)
    print((output2).decode('ascii'))
    print("-"*80)
