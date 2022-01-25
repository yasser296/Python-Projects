from tkinter import Tk , Frame , Label , Menubutton , RAISED , IntVar , Menu



master = Tk()
master.geometry("300x300")

frame = Frame(master)
frame.pack()

menu_bttn = Menubutton( frame , text = "Choose a number :" , relief = RAISED ) 					
#menu_bttn.pack(padx = 10 , pady = 10 )

var_1 = IntVar()
var_2 = IntVar()
var_3 = IntVar()
var_4 = IntVar()
var_5 = IntVar()

menu_1 = Menu( menu_bttn , tearoff = 0 )

menu_1.add_checkbutton( label = "One" , variable = var_1)
menu_1.add_checkbutton( label = "Two" , variable = var_2)
menu_1.add_checkbutton( label = "Three" , variable = var_3)
menu_1.add_checkbutton( label = "Four" , variable = var_4)
menu_1.add_checkbutton( label = "Five" , variable = var_5)

menu_1.add_separator()
menu_1.add("separator")
menu_1.add_separator()

# By using "Radio Button"
menu_1.add_radiobutton( label = "One" , variable = var_1 , value = 1)
menu_1.add_radiobutton( label = "Two" , variable = var_1 , value = 2)
menu_1.add_radiobutton( label = "Three" , variable = var_1 ,  value = 3 )
menu_1.add_radiobutton( label = "Four" , variable = var_1 ,  value = 4 )						
menu_1.add_radiobutton( label = "Five" , variable = var_1 ,  value = 5 )




#menu_bttn.config(menu = menu_1)
menu_bttn["menu"] = menu_1


menu_bttn.pack(padx = 10 , pady = 10 )



















master.mainloop()








