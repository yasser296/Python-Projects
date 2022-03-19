import time # Import time module

start_timer = time.mktime(time.localtime()) # Start time

########## REPLACE ME! #########
big_number = range(10000000)             # Put some function or task to run here

for i in big_number:
    print(i,end=" ")
# print(" ".join(str(i) for i in big_number)) # This is a join method to print the number, can replace above two lines of code
##############################
total_time = time.mktime(time.localtime()) - start_timer # End time minus start time
print("Total time : ", total_time, "seconds") # Total time format
