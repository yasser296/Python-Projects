from tkinter import *

master = Tk()

# master.geometry("width x height") 
# is another way of setting the size for the whole window.                     
master.geometry("300x300")
frame = Frame(master , bd = 50, bg = "green")
frame.pack()

leftframe = Frame(master , bg = "blue", bd = 30)
leftframe.pack(side=LEFT)

rightframe = Frame(master , bg = "red", bd = 5)
rightframe.pack(side=RIGHT)

label = Label(frame, text = "Hello world %d" %5 )
label.pack()

button1 = Button(leftframe, text = "Button1")
button1.pack(padx = 30, pady = 30)

button2 = Button(rightframe, text = "Button2")
button2.pack(padx = 30, pady = 30)

button3 = Button(leftframe, text = "Button3" )
button3.pack(padx = 30 , pady = 30 )

# master.title("text") 
# is used to add a title on the title bar of the window.

master.title("Test_frame")







# master.mainloop() 
# triggers the GUI. Any modifications and widgets 
# to be included should be written before it
master.mainloop()
