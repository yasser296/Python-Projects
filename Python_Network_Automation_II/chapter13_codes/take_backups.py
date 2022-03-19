import getpass
import telnetlib

from datetime import datetime # Import datetime module from datetime library

saved_time = datetime.now().strftime("%Y%m%d_%H%M%S") # Change the format of current time into a string

# Ask for username and password
user = input("Enter your username: ")
password = getpass.getpass()

# Open ip_addresses.txt to read IP addresses
file = open("/root/py_nw_auto_scripts/chapter13_codes/ip_addresses.txt")

# Telnets into Devices & runs show running-config and \
# save it to a file with a timestamp

for ip in file:
    print ("Getting running-config from host IP " + (ip)) # First line print statement for admin
    HOST = ip.strip()
    tn = telnetlib.Telnet(HOST)
    tn.read_until(b"Username: ")
    tn.write(user.encode('ascii') + b"\n")

    if password:
        tn.read_until(b"Password: ")
        tn.write(password.encode('ascii') + b"\n")

   # Makes Term length to 0, run shows commands & reads all output
   # Then saves files with time stamp 
    tn.write(b"terminal length 0\n") # Change terminal length to 0
    tn.write(b"show clock\n") # Disply time
    tn.write(b"show running-config\n") # Show running-configuration
    tn.write(b"exit\n") # Exit session
    readoutput = tn.read_all() # Read output
    saveoutput = open(f"/root/py_nw_auto_scripts/chapter13_codes/backups/{str(saved_time)}_running_config_{HOST}", "wb") # saved_time is the time the file was saved, HOST is the IP address of the device.
    saveoutput.write(readoutput) # Write the output to the file
    saveoutput.close() # Save and close the file
