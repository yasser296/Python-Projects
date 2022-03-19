import re
from netmiko import ConnectHandler
from getpass import getpass
import time

device1 = {                             #Netmiko dictionary for device1
            'device_type' : 'cisco_ios',
            'ip'          : input('IP Address : '),
            'username'    : input('Enter username : '),
            'password'    : getpass('SSH password : '),
          }

net_connect = ConnectHandler(**device1) # Netmiko ConnectHandler object
net_connect.send_command("terminal length 0\n") # Make terminal length to 0 to display all

time.sleep(1) # Pause for 1 second

dir_disk0 = net_connect.send_command("dir disk0:\n") # Send "dir disk0:" command
print(dir_disk0) # Display content of dir flash output

p30 = re.compile(r'D[0-9a-zA-Z]{4}.*.bin') # Regular Expression to capture any file starting with "D", ends with "bin"
m30 = p30.search(dir_disk0) # Search for first match of p30

time.sleep(1) # Pause for 1 second

# net_connect1.enable() (Optional, not required with privilege 15 access)
print("!!! WARNING - You cannot reverse this step.") # Message to user
# If dir_disk0 contains a string which satisfies p30 (True), 
# then run this script to delete a file.
if bool(m30) == True: # If m30 is true
    print("If you can see 'Delete_me.bin' file, select it and press Enter.") # Informational
    del_cmd = "del disk0:/" # Partial command 1
    old_ios = input("*Old IOS (bin) file to delete : ") # Partial command 2, select a file under disk0:
    while (not p30.match(old_ios)) or (old_ios not in dir_disk0): # User input request until correct file name is given
        old_ios = input("**Old IOS (bin) file to delete : ") 
    command = del_cmd + old_ios # Complete command (1 + 2)
    output = net_connect.send_command_timing(   # Special netmiko send_command_timing command with timer
                                                command_string=command,
                                                strip_prompt=False,
                                                strip_command=False
                                            )

    if "Delete filename" in output: # if the returned output contains "Delete filename", send "Enter" (change line)
        output += net_connect.send_command_timing(
                                                    command_string="\n",
                                                    strip_prompt=False,
                                                    strip_command=False
                                                 )
    if "confirm" in output: # if the returned output contains "confirm", send "y"
        output += net_connect.send_command_timing(
                                                    command_string="y",
                                                    strip_prompt=False,
                                                    strip_command=False
                                                 )
    net_connect.disconnect() # Disconnect from SSH session
    print(output) # Informational


# If None (False), then run this script to search directory for .bin file to delete
elif bool(m30) == False: # If no .bin file starting with D is found under "disk0:", run this script
    print("No IOS file under 'disk0:/', select the directory to view.") # Informational

    open_dir = input("*Enter Directory name : ") # Partial command 1
    while not open_dir in dir_disk0: # Ask until correct response is received
        open_dir = input("** Enter Directory name : ") # If file does not exist, request user input again

    open_dir_cmd = (r"dir disk0:/" + open_dir) # Completed command
    send_open_dir = net_connect.send_command(open_dir_cmd) # Send the command
    print(send_open_dir) # Informational

    p31 = re.compile(r'D[0-9a-zA-Z]{4}.*.bin') # Regular Expression to capture any file starting with "D", ends with "bin"
    m31 = p31.search(send_open_dir) # Send completed command

    if bool(m31) == True: # If there is a file with the string satisfy p31 expression
        print("If you see old IOS (bin) in the directory. Select it and press Enter.") # Informational

        del_cmd = "del disk0:/" + open_dir + "/" # Completed command
        old_ios = input("*Old IOS (bin) file to delete : ") # Enter the .bin file to delete

        # User input request until correct file name is given
        while not (p30.match(old_ios)) or (old_ios not in send_open_dir):
            old_ios = input("**Old IOS (bin) file to delete : ")

        command = del_cmd + old_ios # Complete command
        output = net_connect.send_command_timing( # Special netmiko send_command_timing command with timer
                                                    command_string=command,
                                                    strip_prompt=False,
                                                    strip_command=False
                                                )

        if "Delete filename" in output: # if the returned output contains "Delete filename", send "Enter" (change line)
            output += net_connect.send_command_timing(
                                                        command_string="\n",
                                                        strip_prompt=False,
                                                        strip_command=False
                                                     )
        if "confirm" in output: # if the returned output contains "confirm", send "y"
            output += net_connect.send_command_timing(
                                                        command_string="y",
                                                        strip_prompt=False,
                                                        strip_command=False
                                                     )
        net_connect.disconnect() # Disconnect from SSH session
        print(output) # Print content of output
    else: # Both conditions failed to satisfy, exit the script
        ("No IOS found.")
        exit()
    net_connect.disconnect() # Disconnect from SSH session




