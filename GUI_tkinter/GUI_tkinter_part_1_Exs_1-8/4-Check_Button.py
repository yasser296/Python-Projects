from tkinter import Tk , Frame , IntVar ,  Checkbutton , Button


master = Tk()
master.geometry("300x150")

frame = Frame(master)
frame.pack()

var1 = IntVar()
var2 = IntVar()
var3 = IntVar()
var4 = IntVar()

def retrieve() :
	print( var1.get() , "\n" , var4.get() )

ChkBttn = Checkbutton(frame, width = 15, text = "One" ,
			variable = var1 , command = retrieve )			
ChkBttn.pack(padx = 5, pady = 5)

ChkBttn2 = Checkbutton(frame, width = 15 , text = "Two" ,
			variable = var4 , command = retrieve )
ChkBttn2.pack(padx = 5, pady = 5)


#button = Button( master , text = "Submit" , command = retrieve )
#button.pack(padx = 5 , pady = 5 )


master.mainloop()