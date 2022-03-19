import re

output = '''
Yasser>enable                                                                                                                  
Password:                                                                                                                      
Yasser#config t                                                                                                                
Enter configuration commands, one per line.  End with CNTL/Z.                                                                  
Yasser(config)#hostname Yasser                                                                                                 
Yasser(config)#banner motd Hello                                                                                           
Yasser(config)#interface s2/0                                                                                                  
Yasser(config-if)#no shutdown                                                                                                  
Yasser(config-if)#ip address 10.1.2.10 255.255.255.0                                                                           
Yasser(config-if)#exit                                                                                                         
Yasser(config)#exit                                                                                                            
Yasser#exit 
'''

# m = re.findall(r'[#].+\w+\s', output, re.M)
# print(m)
# for i in range(len(m)) : 
# 	k = re.findall(r'[^#].+\w+\s', m[i], re.M)
# 	print(k[0])

#####################################################################################################

# file = open('E:/Yasser/courses/Telecom_and_IT/python_for_networking/mailbox.txt','r')
# r = file.read()

# f = re.findall(r'^[From].+[.]+\w+', r, re.M)
# print(f)

# print('\n\n\n')

# for i in range(len(f)) : 
# 	print(f[i])


# file.close()

#####################################################################################################


# file = open('E:/Yasser/courses/Telecom_and_IT/python_for_networking/mailbox.txt','r')
# r = file.read()

# f = re.findall(r'[\[]+\d+[.]\d+[.]\d+[.]\d+[\]]', r, re.M)
# print(f)

# print('\n\n\n')

# for i in range(len(f)) : 
# 	print(f[i])


# file.close()

#####################################################################################################

# file = open('E:/Yasser/courses/Telecom_and_IT/python_for_networking/mailbox.txt','r')
# r = file.read()

# f = re.findall(r'id .+\w+', r, re.M)
# print(f)

# print('\n\n\n')

# for i in range(len(f)) : 
# 	print(f[i])


# file.close()



#####################################################################################################




file = open('E:/Yasser/courses/Telecom_and_IT/python_for_networking/test.route','r')
r = file.read()

f = re.findall(r'Destination/Mask.+\w+', r, re.M)
for i in range(len(f)) : 
	print(f[i])

print('\n')

f2 = re.findall(r'\w+.\w+.\w+.\w+.\w+. Direct .+\w+', r, re.M)
for i in range(len(f2)) : 
	print(f2[i])

print('\n')

f3 = re.findall(r'\d+.\d+.\d+.\d+/\d+ ', r, re.M)
for i in range(len(f3)) : 
	print(f3[i])

file.close()


