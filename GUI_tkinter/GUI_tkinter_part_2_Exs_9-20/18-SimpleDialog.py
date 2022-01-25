from tkinter import Tk , simpledialog


																							
"""
The SimpleDialog module is used to create dialog 
boxes to take input from the user in a variety of ways.
SimpleDialog allows us to take input of varying 
datatypes from the user, such as float, 
string and integer.

If a tkinter window is not present, 
these functions will create one by default.
"""


master = Tk()

int_input = simpledialog.askinteger("Input" , "Input an integer")
print(int_input)


float_input = simpledialog.askfloat("Input" , "Input a float")
print(float_input)


string_input = simpledialog.askstring("Input" , "Input a string")
print(string_input)









master.mainloop()






