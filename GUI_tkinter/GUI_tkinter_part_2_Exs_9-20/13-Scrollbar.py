"""
Listbox Scrollbar


The first thing to do is create the scrollbar. This scrollbar is then used in the creation of the listbox by passing
it into the yscrollcommand parameter. If you wanted scroll the listbox in the X direction you would use
xscrollcommand instead.


We then generated 100 values and inserted them into listbox. The scrollbar won’t trigger unless the size of
values is greater than the container they are in.


Finally we call the config and assign an additional option called command. The mylist.yview function
activates the listbox’s scroll feature. Use xview or xview depending on the orientation of your widgets
(Horizontal or vertical).

"""




from tkinter import Tk , Label , Scrollbar , RIGHT , LEFT , Y , Listbox , BOTH , END

master = Tk() 
master.geometry("300x300") 

mylabel = Label(master, text ='Scrollbars', font = "30")
mylabel.pack() 

myscroll = Scrollbar(master)
myscroll.pack(side = RIGHT, fill = Y)

mylist = Listbox(master, yscrollcommand = myscroll.set )

for i in range(0, 100):
	#mylist.insert(END, "Number %d" %i)
	mylist.insert(i, "Number %d" %i) 

mylist.pack(side = LEFT, fill = BOTH )

myscroll.config(command = mylist.yview) 


master.mainloop() 






"""
Be careful when packing the Scrollbar. Since typically Scrollbars are on the right, use the side = RIGHT
option and to ensure the scrollbar fills the screen, use the fill = Y 
(though you may want to alter this in some scenarios)

"""









######################################################################################################
######################################################################################################
######################################################################################################












"""
Canvas Scrollbar
As a bonus, we’ve created two scroll bars this time, just to show you it’s possible. You likely won’t be using
this in an actual GUI.

Notice the many expand = True options. Try re-sizing the Tkinter frame with these on, then remove them
and try again.

The last new feature here is the scroll region for the Canvas. It’s total size is technically 500 by 500, but only
300 by 300 is viewable at any given time. The scroll region should always be larger than the width and height.
Ruins the purpose otherwise.
"""



# from tkinter import *

# master = Tk()

# frame = Frame(master,width=300,height=300)
# frame.pack(expand = True, fill=BOTH)

# canvas = Canvas(frame,bg='white', width = 300,height = 300, scrollregion=(0,0,500,500))

# hbar = Scrollbar(frame,orient = HORIZONTAL)
# hbar.pack(side = BOTTOM, fill = X)
# hbar.configure(command = canvas.xview)

# vbar = Scrollbar(frame,orient = VERTICAL)
# vbar.pack(side = RIGHT, fill = Y)
# vbar.config(command = canvas.yview)

# canvas.config(width = 300,height = 300)
# canvas.config(xscrollcommand = hbar.set, yscrollcommand = vbar.set)

# canvas.pack(side = LEFT, expand = True, fill = BOTH)

# master.mainloop()


