count = 0
def tower(num , source , auxiliary , destination):
	global count
	if num == 1 :
		print("\nMove disk 1 from" , source , "to", destination ) # Base case
		count = count + 1
		return
	
	tower(num-1 , source , destination , auxiliary)
	print("move disk" , num , "from" , source , "to" , destination)
	count = count + 1
	tower(num-1 , auxiliary , source , destination)




tower( 4 , 'A' , 'B' , 'C' )
print("\n\n\n" , "Total number of moves: " , count)











































