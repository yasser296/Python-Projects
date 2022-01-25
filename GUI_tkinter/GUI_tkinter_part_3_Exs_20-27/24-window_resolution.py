"""
The first way is using the call() function to 
change the resolution scaling

"""




#from tkinter import Tk , Frame , Label 



#master = Tk()
#master.geometry("300x300")

#frame = Frame(master)
#frame.pack()


#label = Label(frame , text = "Hello world!" )
#label.pack()


#master.call( "tk" , "scaling" , 2.0 )



#"""

#Keep in mind this will also effect the size of 
#the tkinter window. Basically, you increasing 
#the pixel density by increasing scaling, hence 
#you will have to increase the number of pixels 
#to maintain the same size as before.


#2.0 was merely the value we used. 
#You can change this value to see what suits you best.

#"""




#master.mainloop()








#=====================================================
#=====================================================
#=====================================================






"""

The second method is the use of the ctypes Python library. 
This following setting in the ctypes library sets

“DPI” awareness. DPI stands for Dots per inch, 
another way of measuring screen resolution.


"""




import tkinter as tk

import ctypes
from ctypes import *


ctypes.windll.shcore.SetProcessDpiAwareness(1)


root = tk.Tk()

root.geometry("200x150")

label = tk.Label(root, text = "Hello World")
label.pack(padx = 10 , pady = 10)




root.mainloop()




