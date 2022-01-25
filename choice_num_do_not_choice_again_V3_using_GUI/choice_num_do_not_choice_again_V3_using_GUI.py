"""																														
This code creates a list of number from 1 to what ever you want,
and then choice a random number from the list and store 
it to a text file, then choice again a random number, 
and also store it in the same text file, but every time 
it choice any number the code opening the text file and 
compare the chosen random number by the numbers that 
stored earlier in the same text file.

After the ending from the all numbers on the text file 
the code will automatically delete all numbers on the 
text file.

Every time you run the code it will read and compare 
then at the end it will delete all numbers.

Yasser Ahmad Tolba 
Alexandria
Egypt


"""



from tkinter import Tk , ttk , Frame , Label , Entry , Button , Canvas , Scrollbar , RIGHT , LEFT , Y , X , BOTH , END , HORIZONTAL , BOTTOM , VERTICAL
from random import choices
from time import sleep

# file_name = "text.txt"
file_name = "E:/python_projects/choice_num_do_not_choice_again/choice_num_do_not_choice_again_V3_using_GUI/text.txt"

master = Tk()

# #Clear all on the text file at start
# file = open(file_name , "w")
# file.write("")
# file.close()


list_2 = list()



def yes() :
	max_num = entry_1.get()
	
	list_num = list()
	for i in range(1 , int(max_num)+1) :
		list_num.append(i)
		
	#label_2 = Label(master , text = "The list of numbers that created : \n %s \n " %list_num )
#	label_2.pack()
	
	
	choose_num = choices(list_num)
	

	file_read = open(file_name , "r")
	for line in file_read :
		list_2 = line.split()
		#print(list_2)
				
	file_read.close()

	counter = 0
	counter_2 = 0
		
	if str(choose_num[0]) in list_2 :
		while True :
			choose_num = choices(list_num)
			if str(choose_num[0]) not in list_2 :
				counter += 1
				counter_2 = 0
				break    # end the "while True" loop
			if len(list_2) == len(list_num) :
				counter_2 = 0
				break
			counter_2 += 1
			if counter_2 > len(list_num)*2 :
				break
					
	file = open(file_name , "a")
	counter += 1
	file.write(str(choose_num[0]))
	file.write(" ")
	file.close()
	
	if str(choose_num[0]) not in list_2 :
		entry_2 = Entry(sub_frame, width = 80)
		entry_2.insert( 0 , "The random number from the list is : %s " % choose_num[0])
		entry_2.pack(padx = 5, pady = 5)
	
	
	if len(list_2) >= len(list_num) :
		label_3 = Label(sub_frame , text = f"You now finished from the {len(list_num)} numbers on the list. \n"  )        
		label_3.pack(padx = 5, pady = 5)
		label_4 = Label(sub_frame , text = "Now all the numbers on the file %s are deleted. \n" % file_name)
		label_4.pack()
		label_5 = Label(sub_frame , text = "You can now run the code again \nto simply play again :), enjoy!\n")
		label_5.pack()
			
		file = open(file_name , "w")
		file.write(" ") #you must write "space" to make list_2 read something.
		file.close()
		#list_2 = [0]
		
		#sleep(3)
		#master.after(3000)    # after() is the better choice
		
		label_6 = Label(sub_frame , text = "The GUI master will destroy \nthe program after 5 seconds.")
		label_6.pack()
		#sleep(5)
		#master.destroy()
		#master.quit()
		# master.after(5000 , no )     # after() is the better choice
	
	
		
	f = open(file_name, "r")
	print(f.read())
	f.close()

def no():
	print("It is the end! \nYou can run the code again later to simply play again :), enjoy! \n")
	master.destroy()
		





master.geometry("500x500")

frame = Frame(master,width=500,height=500)
frame.pack(expand = True, fill=BOTH)



canvas = Canvas(frame, width = 30,height = 30 )

h_bar = ttk.Scrollbar(frame , orient = HORIZONTAL)
h_bar.configure(command = canvas.xview)
h_bar.pack(side = BOTTOM, fill = X)

v_bar = ttk.Scrollbar(frame,orient = VERTICAL)
v_bar.config(command = canvas.yview)
v_bar.pack(side = RIGHT, fill = Y)

canvas.config(width = 300,height = 300)
canvas.config(xscrollcommand = h_bar.set , yscrollcommand = v_bar.set)

canvas.bind('<Configure>' , lambda e: canvas.configure(scrollregion=(0,0,5000,5000)))
scrollregion = canvas.bbox("all")
canvas.pack(side = LEFT, expand = True, fill = BOTH)


sub_frame = Frame(canvas)


canvas.create_window((0,0) , window = sub_frame , anchor = "nw")






label = Label(sub_frame, text = "Please enter the maximum number of members : ")
label.pack()

entry_1 = Entry(sub_frame, width = 30)
entry_1.insert( 0 , " " )
entry_1.pack(padx = 10 , pady = 10 )



label_3 = Label(sub_frame, text = "Do you want to choose a number : ")
label_3.pack()


button_1 = Button(sub_frame, text = "Choice a number", command = yes )
button_1.pack(padx = 5, pady = 5)


button_2 = Button(sub_frame, text = "End the game", command = no )
button_2.pack(padx = 5, pady = 5)





# canvas.pack(side = LEFT, expand = True , fill = BOTH)






master.title("Choose a number game")
master.iconbitmap('E:/python_projects/choice_num_do_not_choice_again/choice_num_do_not_choice_again_V3_using_GUI/clips2.ico')
# master.attributes('-fullscreen', True)
master.mainloop()







