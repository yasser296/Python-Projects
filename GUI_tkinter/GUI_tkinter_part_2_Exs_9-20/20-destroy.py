from tkinter import *


def delete():
	mylabel.destroy()

		
def close():
	master.destroy()


master = Tk()
master.geometry('150x100')

mylabel = Label(master, text = "This is some random text")
mylabel.pack(pady = 5)

mybutton = Button(master, text = "Delete", command = delete)
mybutton.pack(pady = 5)

button = Button(master, text = 'Close the window', command = close)					
#button = Button(master, text = 'Close the window', command = master.destroy) # it could work
button.pack(pady = 10)







master.mainloop()




