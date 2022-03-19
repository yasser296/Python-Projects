import socket

ip = ‘192.168.183.101’

def check_port_22(): # Define a function
    for port in range (22, 23): # port 22
        dest = (ip, port) # new tuple variable
        try: # using try & except, we can avoid check process being stuck in a loop
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
                s.settimeout(3)
                connection = s.connect(dest) # Connect to socket
                print(f"On {ip}, port {port} is open!") # Informational
                print("OK - This device is on the network.") # Informational
        except:
            print(f"On {ip}, port {port} is closed. Exiting!") # Informational
            print("! FAILED - to reach the device. Check the connectivity to this device") # Informational
            exit() # Exit application
check_port_22() # Run the function
