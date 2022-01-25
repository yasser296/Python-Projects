from tkinter import *

master = Tk()

frame = Frame(master,width=300,height=300)
frame.pack(expand = True, fill=BOTH)

canvas = Canvas(frame,bg='white', width = 300,height = 300, scrollregion=(0,0,500,500))

hbar = Scrollbar(frame,orient = HORIZONTAL)
hbar.pack(side = BOTTOM, fill = X)
hbar.configure(command = canvas.xview)

vbar = Scrollbar(frame,orient = VERTICAL)
vbar.pack(side = RIGHT, fill = Y)
vbar.config(command = canvas.yview)

canvas.config(width = 300,height = 300)
canvas.config(xscrollcommand = hbar.set, yscrollcommand = vbar.set)

bttn = Button(frame)
bttn.pack()

canvas.pack(side = LEFT, expand = True, fill = BOTH)

master.mainloop()
