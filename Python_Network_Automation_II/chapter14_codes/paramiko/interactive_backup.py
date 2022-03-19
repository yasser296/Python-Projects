import re # import regular expression module
import time # import time module
import paramiko # import paramiko library
from datetime import datetime # import datetime module from datetime library
from getpass import getpass # Import getpass module from getpass library

t_ref = datetime.now().strftime("%Y-%m-%d_%H-%M-%S") # Time reference to be used for file name

device_list = ["192.168.110.140", "192.168.110.200", "192.168.110.201", "192.168.110.202", "192.168.110.203"]

start_timer = time.mktime(time.localtime()) 

def get_credentials():
    #Prompts for, and returns a username and password
    global username # Make username global, so it can be used throughout this script
    global password # Make password global, so it can be used throughout this script
    username = input("*Enter Network Admin ID : ") 
    password = None # set password default value to None
    while not password: # Until password is entered
        password = getpass("*Enter Network Admin PWD : ") # Enter the password first time
        password_verify = getpass("**Confirm Network Admin PWD : ") # Get password for verification, second time
        if password != password_verify: # Password verification
            print("! Network Admin Passwords do not match. Please try again.") # Informational
            password = None # Set password to None
    return username, password # Optional, returns username and password

get_credentials()# Run get_credentials function, to save username and password

for ip in device_list: # for loop to grab device IP addresses
    print(t_ref) # Comment for user information
    print("Now logging into " + (ip)) # Informational
    ssh_client = paramiko.SSHClient()# Initiate paramiko SSH client session as ssh_client
    ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy()) # Accept missing host key policy
    ssh_client.connect(hostname=ip,username=username,password=password) # SSH connection with credentials

    print("Successful connection to " + (ip) +"\n") # Informational
    print("Now making running-config backup of " + (ip) + "\n") # Comment for user information
    remote_connection = ssh_client.invoke_shell() # Invoke shell
    time.sleep(1) # Pause 3 seconds to invoke shell
    remote_connection.send("copy running-config tftp\n") # Send copy command
    remote_connection.send("192.168.110.133\n") # Respond to TFTP server IP request, TFTP IP 
    remote_connection.send((ip)+ ".bak@" + (t_ref)+ "\n") # Respond to backup file name request
    time.sleep(1) ## Pause for 3 seconds, give device to respond
    print() # Print screen
    time.sleep(1) # Pause for 3 seconds, give time to process data
    output = remote_connection.recv(65535) # Receive output up to 65535 lines
    print((output).decode('ascii')) #Print output using ASCII decoding method

    print(("Successfully backed-up running-config to TFTP & Disconnecting from ") + (ip) + "\n") # Print statement to provide an update to the user
    print("-"*80) # Print ~ 80 times
    print("-"*80) # Print ~ 80 times
    print("-"*80) # Print ~ 80 times
    ssh_client.close # Close SSH session
    time.sleep(1) # Pause for 1 second

total_time = time.mktime(time.localtime()) - start_timer # Start time minus current time
print("Total time : ", total_time, "seconds") # Print the total time to run the script in seconds
