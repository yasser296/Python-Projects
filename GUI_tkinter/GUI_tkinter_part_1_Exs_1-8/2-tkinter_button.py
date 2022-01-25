#from tkinter import *

#def set():
#	print("Hello World")

#master = Tk()
#master.geometry("200x150")

#frame = Frame(master)
#frame.pack()

#button = Button(frame, text = "Button1", command = set)
#button.pack()

#master.mainloop()


#####################################################################
####################=##=########################=###########



from tkinter import *

def set():
	print("Hello World")

master = Tk()
master.geometry("200x150")

frame = Frame(master)
frame.pack()

button = Button(frame, text = "Button1", command = set ,
			 fg = "red", font = "Verdana 14 underline",
			 bd = 2, bg = "light blue", relief = "groove")
button.pack(pady = 40 , padx = 10)



def end() :
	print("This is the end")
	master.destroy()
	


button_2 = Button( frame , text = "End" , command = end )
button_2.pack()

master.mainloop()




