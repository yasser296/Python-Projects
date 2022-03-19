import socket
import time
from datetime import datetime

# Custom module
from send_email import send_email # import send_email module from email_send.py

starttime = time.time()

# Variables
ip = "192.168.183.101"
port = 22
dest = (ip, port)

def check_sw1(): # Define check_sw1 function
    counter = 0 # Set counter’s original value to 0
    while (counter < 10): # Run the script until counter 10 is reached
        f = open('./monitoring_logs.txt', 'a') # Open monitoring logs file for record in appending mode
        try: # This is basically the same code as check_port_22.py
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
                s.settimeout(3)
                connection = s.connect(dest)
                counter = 0 # Reset the counter to 0 on successful check
                counter1 = str(counter) # convert counter to string
                f.write(datetime.now().strftime('%Y-%m-%d %H:%M:%S')) # Write time to file
                print(f" {counter1} port {port} is open") # Informations for console user
                f.write(f" {counter1} port {port} is open\n") # Write to log file for task completion
                f.close() # close file
                time.sleep(3) # Wait for 3 seconds before another check
        
        except: # If port 22 is closed
            counter += 1 # Adds 1 to counter every loop
            counter2 = str(counter) # convert counter to string
            f.write(datetime.now().strftime('%Y-%m-%d %H:%M:%S')) # Write time to file
            print(f" {counter2} port {port} is closed") # Informations for console user
            f.write(f" {counter2} port {port} is closed\n") # Write to log file for task completion
            time.sleep(3) # Wait for 3 seconds before another check
            if counter == 10: # Check if counter is 10
                counter=0 # Only resets the counter to 0 on 10th time
                print("send failed email here") # Informations for console user
                send_email() # Send an email notification, calling send_email() from send_email.py script
            f.close()# close file

check_sw1() # Run check_sw1 function
