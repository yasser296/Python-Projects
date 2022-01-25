from tkinter import Tk , StringVar , IntVar , Frame , Radiobutton



master = Tk()
master.geometry("300x300")

frame = Frame(master)
frame.pack()


var1 = StringVar()
#var1 = IntVar()


def retrieve() :
	print(var1.get())
	print(type(var1))
	print(type(var1.get()))

RBttn_1 = Radiobutton(  master , text = "One" , variable = var1 ,
				value = 1 , command = retrieve , justify = "left")													
RBttn_1.pack(padx = 10 , pady = 10 )


RBttn_2 = Radiobutton(  master , text = "Two" , variable = var1 ,
				value = 2 , command = retrieve )
RBttn_2.pack(padx = 10 , pady = 10 )


RBttn_3 = Radiobutton(  master , text = "Three" , variable = var1 ,
				value = 3 , command = retrieve )
RBttn_3.pack(padx = 10 , pady = 10 )


RBttn_4 = Radiobutton(  master , text = "Four" , variable = var1 ,
				value = 4 , command = retrieve )
RBttn_4.pack(padx = 10 , pady = 10 )




master.mainloop()



