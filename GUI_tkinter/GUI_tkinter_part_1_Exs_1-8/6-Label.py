from tkinter import Tk , Frame , Label , LEFT , StringVar , Button


master = Tk()
master.geometry("300x300")

frame = Frame(master)
frame.pack( side=LEFT , padx = 10 , pady = 10 )

var = StringVar()
var.set("Hello world! :)")

def set() :
	var.set("Goodbye world! :( ")
		
def changecolor() :
	label.configure(fg = "blue" )

label = Label(frame , fg = "red" , textvariable = var )
label.pack( padx = 10 , pady = 10 )

set_button = Button(frame , text = "set" , fg = "red" , command = set )
set_button.pack( padx = 10 , pady = 10 )


set_color = Button(frame , text = "set color" , fg = "green" , command = changecolor )
set_color.pack( padx = 10 , pady = 10 )





master.mainloop()													





