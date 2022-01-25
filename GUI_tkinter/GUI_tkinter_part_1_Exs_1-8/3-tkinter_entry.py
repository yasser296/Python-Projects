from tkinter import * 



master = Tk()
master.geometry("200x150")

frame = Frame(master)
frame.pack()

entry_1 = Entry(frame, width = 20)
entry_1.insert(0,'Username')
entry_1.pack(padx = 5, pady = 5)

entry_2 = Entry(frame, width = 15)
entry_2.insert(0,'password')
entry_2.pack(padx = 5, pady = 5)

a = 0


def increase():
	file = open("memory.txt" , "r")
	for line in file :
		a = int( line.split()[0] )
		print(a,type(a))
	file.close()

	a += 1
	file = open("memory.txt" , "w")
	file.write(str(a))
	file.close()
	print("Hello World")
	entry_1.delete(0,20)
	entry_1.insert(0 , "Hello World %d" %a )

	

button_1 = Button(master , text = "Increase 1" , command = increase )
button_1.pack()



def decrease():
	file = open("memory.txt" , "r")
	for line in file :
		a = int( line.split()[0] )
		print(a,type(a))
	file.close()

	a -= 1
	file = open("memory.txt" , "w")
	file.write(str(a))
	file.close()
	print("Hello World")
	entry_1.delete(0,20)
	entry_1.insert(0 , "Hello World %d" %a )
	


button_2 = Button(master , text = "Decrease 1 " , command = decrease )
button_2.pack()



master.mainloop()




#####################################################################
####################=##=########################=###########



# from tkinter import *


# def retrieve():
# 	a = int(my_entry.get())
# 	print(a)
# 	print(my_entry2.get())
	
# 	print(type(a))
# 	print(type(my_entry2.get()))


# master = Tk()
# master.geometry("200x150")

# frame = Frame(master)
# frame.pack()


# my_entry = Entry(frame, width = 30)
# my_entry.insert( 0 , 'Username')
# my_entry.pack(padx = 10 , pady = 10 )

# my_entry2 = Entry(frame, width = 15)
# my_entry2.insert( 0 , 'password')
# my_entry2.pack(padx = 20 , pady = 20)


# my_entry3 = Entry(frame, width = 15)
# my_entry3.insert( 0 , "")
# my_entry3.pack(padx = 20 , pady = 20)

 

# Button = Button(frame, text = "Submit", command = retrieve)
# Button.pack(padx = 5, pady = 5)



master.mainloop()





