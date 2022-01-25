#from tkinter import Tk ,Toplevel




#master = Tk()
#window = Toplevel()

#master.mainloop()




######################################################################################################
######################################################################################################
######################################################################################################




from tkinter import Tk , Toplevel , Frame , Label , Button 



def new_window():
	window = Toplevel()
	window.geometry('500x300')
	
	newlabel = Label(window, text = "Settings Window")
	newlabel.pack()
	
	window.title("Settings Window")
	
	a = window.frame()
	print(a)
	
	destroy_bttn = Button(window , text = "Destroy Settings window" , command = window.destroy) 			 
	destroy_bttn.pack(pady = 10 , padx =10 )


master = Tk()
master.geometry("300x300")

frame = Frame(master)
frame.pack()

bttn = Button(frame, text = "Settings", command = new_window)
bttn.pack(pady = 10 , padx =10 )


master.title("Main Window")





master.mainloop()



















