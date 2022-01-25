#purse = dict()
#purse['money'] = 5
#purse['a'] = 63
#purse['b'] = 94
#print(purse)
#print(purse['b'])
#purse['a'] += 2
#print(purse)



#===========================================================================
#===========================================================================
#===========================================================================


#aaa = {'a' : 1 , 'b' : 40 , 'c' : 90 }
#bbb = {} 
#print(aaa,'\n', bbb)
#	#print(aaa['f'])  # KeyError: 'f'
#print('f' in aaa)
# 



#===========================================================================
#===========================================================================
#===========================================================================



#  # count the words

#counts = dict()
#words = ['a' , 'a' , 'b' , 'c' , 'v' , 'b' , 'c' , 'b' , 'b' ]
#for word in words :
#	if word not in counts :
#		counts[word] = 1
#	else:
#		counts[word] = counts[word] + 1 
#print(counts)



#  # or we can use get() to count

#counts_2 = dict()
#for word in words : 
#	counts_2[word] = counts_2.get(word,0) + 1 
#print(counts_2)




#counts = dict()
#print('Enter a line of text: ')
#line = input()
#words = line.split()
#print('words: ' , words)
#print('counting...')
#for word in words :
#	counts[word] = counts.get(word,0)+1
#print("counts : " , counts )







	# counts the words using pprint() function 
	# pprint() is like the normal print() but it for dictionaries

#import pprint

#counts = dict()
#words = ['a' , 'a' , 'b' , 'c' , 'v' , 'b' , 'c' , 'b' , 'b' ]
#for word in words :
#	if word not in counts :
#		counts[word] = 1
#	else:
#		counts[word] = counts[word] + 1 
#print(counts)

#pprint.pprint(counts)

#for item in counts:
#	print(item , counts[item])
#	


#===========================================================================
#===========================================================================
#===========================================================================



 #  # Definite loops and dictionary

#aaa = {'a' : 1 , 'b' : 40 , 'c' : 90 }
#for key in aaa :
#	print(key,aaa[key])




#===========================================================================
#===========================================================================
#===========================================================================

#   # retrieving lists of keys and values
#   
#aaa = {'a' : 1 , 'b' : 40 , 'c' : 90 }
#print(list(aaa))
#print(aaa.keys())
#print(aaa.values())
#print(aaa.items())




#===========================================================================
#===========================================================================
#===========================================================================


#	# two iteration variables
#aaa = {'a' : 1 , 'b' : 40 , 'c' : 90 }
#for aaa , bbb in aaa.items() :
#	print(aaa,bbb)



#===========================================================================
#===========================================================================
#===========================================================================




#	# to read from file
#	# using two nested loops
#	
#handle = open("test_text.txt")
#counts = dict() 

#for line in handle :
#	words = line.split()
#	for word in words:
#		counts[word] = counts.get(word,0) + 1
#		
#print(counts)		

#bigcount = None
#bigword = None

#for word , count in counts.items():
#	if bigcount is None or count > bigcount :
#		bigcount = count
#		bigword = word 

#print(bigword , bigcount)






#===========================================================================
#===========================================================================
#===========================================================================




	# Task 

	# Write a script to read through the mailbox.txt and 
	# figure out who has sent the greatest number of mail 
	# messages. 

	# The script looks for 'From ' lines and takes 
	# the second word of those lines as the person 
	# who sent the mail. 

	# The script creates a Python dictionary that maps 
	# the sender's mail address to a count of the number 
	# of times they appear in the file.

	# After the dictionary is produced, the script 
	# reads through the dictionary using a maximum loop 
	# to find the most prolific committer.


  
file = open("mailbox.txt" , "r")
counter = dict()
for line in file :
	if line.startswith("From "):
		print (line)
		email = line.strip().split("From ")[1].split()[0]
		print(email)
		name = email.split("@")[0]
		print(name)
		
		counter[name] = counter.get(name,0) + 1
		
		print("\n\n\n")		
		
print(counter , "\n")


bigcount = the_name = None

for name , count in counter.items():
	if bigcount is None or count > bigcount :
		bigcount = count
		the_name = name 

print("The person who has sent the greatest number of mail massages : ", the_name )
print("where the greatest number of mail massages : " , bigcount)




