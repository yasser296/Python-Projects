from tkinter import Tk , Frame , Label , Listbox , Button , END



master = Tk()
master.geometry("300x300")

frame = Frame(master)
frame.pack()

label = Label(frame , text = "A List of numbers : " )
label.pack(padx = 10 , pady = 10)


def retrieve() :
	index = list_box.curselection()
	print(index)
	print(type(index) , "\n" )
	print(index[0])
	print(type(index[0]) , "\n\n" )
	
	
def get_items():
	items = list_box.get( 0 , END )
	print(items , "\n" )
	print(type(items))
	print(type(items[0]))
	length = len(items)
	print( "Length of the tuple = %d " %length)
	for i in range(0 , length ) :
		print(items[i])


list_box = Listbox(frame) # or master , any way as long as the frame is in "master" (i.e. frame = Frame(master) ) it will work, but try to change it if there is any problem.           
#list_box.insert( -1 , "Negative One" )   # with "insert( 0 , "Zero" )" the index = 6 (the last index), without it the index = 0.
list_box.insert( 0 , "Zero" )
list_box.insert( 1 , "One" )       # # with "insert( 0 , "Zero" )" the index = 1 (the 2nd index), without it the index = 0.
list_box.insert( 2 , "Two" )
list_box.insert( 3 , "Three" )
list_box.insert( 4 , "Four" )
list_box.insert( 5 , "Five" )

list_box.insert( 6 , "Zero" )
list_box.insert( 7 , "One" )      
list_box.insert( 8 , "Two" )
list_box.insert( 9 , "Three" )
list_box.insert( 10 , "Four" )
list_box.insert( 11 , "Five" )
list_box.pack()



bttn = Button( master , text = "Submit" , command = retrieve )
bttn.pack( side = "bottom" )


bttn = Button( master , text = "Get items" , command = get_items )
bttn.pack( side = "bottom" )



master.mainloop()










