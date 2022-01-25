"""

Tkinter grid – layout management

In this article we’ll be covering the Tkinter grid 
layout manager. 

Tkinter grid is one out of three layout managers 
used to control the placement of widgets on a 
Tkinter window.


The other two layout managers are pack() and place(). 
In this article however, we’ll simply cover Tkinter
grid and it’s various usages.


create a spread-sheet like window through 
the use the Entrybox and grid system.

"""

from tkinter import *




master = Tk()
master.geometry('300x300')



for x in range(10):
	for y in range(6) :
		entry = Entry(master, width = 6)
		entry.grid(row = x, column = y)




master.mainloop()