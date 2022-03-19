#---------------------------------------------------# Import required modules
import time                                          
import socket
import difflib
from getpass import getpass
from netmiko import ConnectHandler

#---------------------------------------------------# Borrowed from previous labs

# Functions to collect credentials and IP addresses of devices
def get_input(prompt=''):
    try:
        line = input(prompt)
    except NameError:
        line = input(prompt)
    return line

def get_credentials():
    #Prompts for, and returns a username and password
    username = get_input("Enter Network Admin ID     : ")
    password = None
    while not password:
        password = getpass("Enter Network Admin PWD    : ")
        password_verify = getpass("Confirm Network Admin PWD   : ")
        if password != password_verify:
            print("Passwords do not match. Please try again.")
            password = None
    return username, password

# For IP addresses of comparing devices
def get_device_ip():
    #Prompts for, and returns a first_ip and second_ip
    first_ip = get_input("Enter primary device IP      : ")
    while not first_ip:
        first_ip = get_input("* Enter primary device IP     : ")
    second_ip = get_input("Enter secondary device IP    : ")
    while not second_ip:
        second_ip = get_input("* Enter secondary device IP : ")
    return first_ip, second_ip
#--------------------------------------------------------------------------------

# Run the functions to collect credentials and ip addresses
print("-"*40)
username, password = get_credentials()
first_ip, second_ip = get_device_ip()
print(first_ip , "\n" , second_ip)
print("-"*40)

#--------------------------------------------------------------------------------
# Netmiko device dictionaries
device1 = {                     # Netmiko dictionary for device1
            'device_type': 'cisco_ios',
            'ip': first_ip,
            'username': username,
            'password': password,
          }

device2 = {                     # Netmiko dictionary for device2
            'device_type': 'cisco_ios',
            'ip': second_ip,
            'username': username,
            'password': password,
          }

devices = [device1, device2]

#--------------------------------------------------------------------------------
# Re-use port scanner as a pre-check tool for reachability verification tools.
# If an IP is not reachable, the application will exit due to a communication problem.

for device in devices: # Loop through   devices
    ip = device.get("ip", "") # get value of the key "ip"
    for port in range (22, 23): # only port 22
        dest = (ip, port) # Combine ip and port number to form dest object
        try:
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
                sock.settimeout(3)
                connection = sock.connect(dest)
                print(f"on {ip}, port {port} is open!")
        except:
            print(f"On {ip}, port {port} is closed. Check the connectivity to {ip} again.")
            exit()

# Prompt the user to make a decision to run the tool
response = input(f"Make a comparison of {first_ip} and {second_ip} now? [Yes/No]")
response = response.lower()
if response == 'yes' or response == 'y'  :
    print(f"* Now making a comparison : {first_ip} vs {second_ip}") # Informational
    for device in devices: # Loop through   devices
        ip = device.get("ip", "") # Get value of the key "ip"
        try:
            net_connect = ConnectHandler(**device) # Create netmiko connection object
            net_connect.send_command("terminal length 0\n")
            output = net_connect.send_command("show running-config\n") # Run show running config
            show_run_file = open(f"{ip}_show_run.txt", "w+") # Create a file
            show_run_file.write(output) # Write output to file
            show_run_file.close() # Close-out the file
            time.sleep(1)
            net_connect.disconnect() # Disconnect SSH connection
        except KeyboardInterrupt: # Keyboard Interrupt
            print("-"*80)
else:
    print("You have selected No. Exiting the application.") # Informational
    exit()

#--------------------------------------------------------------------------------
# Compare the two show running config files and display it in html file format. # Informational
# Prepare for comparison of the text files
device1_run = f"./{first_ip}_show_run.txt" # Create device1_run object, ./ is present working folder
device2_run = f"./{second_ip}_show_run.txt" # Create device2_run object
device1_run_lines = open(device1_run).readlines() # Convert into strings first for comparison
time.sleep(1)
device2_run_lines = open(device2_run).readlines() # Convert into strings first for comparison
time.sleep(1)

# Four arguments required in HtmlDiff function
difference = difflib.HtmlDiff(wrapcolumn=60).make_file(device1_run_lines, device2_run_lines, device1_run, device2_run)
difference_report = open(first_ip + "_vs_" + second_ip + "_compared.html", "w") # Create html file to write the difference
difference_report.write(difference) # Writes the differences to the difference_report
difference_report.close()
print("** Device configuration comparison completed. Please Check the html file to check the differences.")
print("-"*80)
time.sleep(1)




