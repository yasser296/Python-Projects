import  socket  # Import socket module

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # Create a socket object

#dest = ("192.168.110.140", 80) # IP and Port to scan 
dest = ("192.168.110.140", 22) # IP and Port to scan 
port_open = sock.connect_ex(dest) # Create socket connect object

# open returns int 0, closed returns an integer based on port number
if port_open == 0: # If port is opened, it returns 0
    print(port_open) # print result = 0
    print("On ", {dest[0]}, "port is open.") # Informational
else:
    print(port_open) # print result, an integer other than 0
    print("On ", {dest[0]}, "port is closed.") # Informational
sock.close() # close socket object
