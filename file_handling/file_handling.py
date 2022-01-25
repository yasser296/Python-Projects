# file = open("ted.txt")
# print(file)
# print()
# print()


# for word in file :
# 	print(word)
	
# ###############################################################
# ###############################################################
# ###############################################################

# counter = 0
# for every_line in file :
# 	counter += 1
# print("number of lines:  " , counter)

# ###############################################################
# ###############################################################
# ###############################################################

# #reading the whole file including newlines and all
# var = file.read()
# print(var)
# print()
# print(len(var))
# print(var[ : 100])

# ###############################################################
# ###############################################################
# ###############################################################

# # print one litter in every newline
# for line in var :
# 	print(line)

# ###############################################################
# ###############################################################
# ###############################################################

# # print line by line
# var2 = file.readlines()
# for line in var2 :
# 	print(line)

# ###############################################################
# ###############################################################
# ###############################################################

# for line in file :
# 	line = line.rstrip()
# 	if line.startswith( "0" ) :
# 		print( line )	
		
# 	if line.startswith( "1" ) :
# 		print( line )
		
# 	if line.startswith( "2" ) :
# 		print( line )

# ###############################################################
# ###############################################################
# ###############################################################

# for line in file:
# 	line = line.rstrip()
# 	if not line.startswith( '1' ):
# 		continue
# 	print(line)

# ###############################################################
# ###############################################################
# ###############################################################

# for line in file :
# 	line = line.rstrip()
# 	if not 'five' in line :
# 		continue
# 	print(line)

# ###############################################################
# ###############################################################
# ###############################################################

# input = input("Enter the file name :  ")

# try:
# 	file = open(input) 
# except:
# 	print("The file cannot be opened :  " , input )

# counter = 0 
# for line in file:
# 	if line.startswith("0"):
# 		counter += 1 
# 		line = line.rstrip()
# 		print(counter , "	" ,  line )
		
# print("There were " , counter , " time lines starts with 0  in " , input)



###############################################################
###############################################################
###############################################################

# Parse ‘test.route’ file and extract the
# number of routes with its type (static, direct, etc..)
 
show = open("test.route")
var = show.read()
print(show, "\n") 
print(var, "\n")

file = open("test.route")  # you must open the file again after the ".read()" function 
static = 0
direct = 0
for line in file:  
        # reading each word            
        for word in line.split(): # you can delete this line, but it make the solution easy-to-use
            # searching about the words
            if "Static" == word:
            	static += 1
            if "Direct" in word: 
            	direct += 1
                     
print("The number of Static = " , static)
print("The number of Direct = " , direct , "\n\n\n")
file.close()


print("### ==================another solution===================== ### \n\n\n")


import collections

file = open("test.route")
counter = 0
route_type =[]
for line in file :
	if "/" in line :
		if "Mask" in line :
			continue
		else :
			counter += 1
			route_type.append(line.strip().split("/")[1][2: ].lstrip().split()[0])
			print(line.strip().split("/")[1][2:].lstrip().split()[0])
			


print("\n" "Number of routes = " , counter , "\n")


routes_counter = str(collections.Counter(route_type))
print(route_type , "\n")
print(routes_counter , "\n")

routes_counter_2 = routes_counter.replace("Counter({" , "").replace("})" , "").split(",")
for route in routes_counter_2 :
	print(route.strip())

file.close()

 





