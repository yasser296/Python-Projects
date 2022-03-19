import  socket # Import socket module

ip_addresses = ["192.168.110.140", "192.168.110.200", "192.168.110.201", "192.168.110.202", "192.168.110.203"] 

for ip in ip_addresses: # get ip from the list, ip_addresses
    for port in range (22, 24): # port range, ports 22-23, always n-1 for the last digit
        dest = (ip, port) # combine both ip and port number into one object as socket method takes 1 attribute
        try: # Use try except method
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock: # s as a socket object
                sock.settimeout(3)
                connection = sock.connect(dest) # connect to destination on specified port
                print(f"On {ip}, port {port} is open!") # Informational
        except:
            print(f"On {ip}, port {port} is closed.") # Informational
