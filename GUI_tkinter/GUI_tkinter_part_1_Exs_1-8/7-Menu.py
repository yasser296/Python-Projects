#from tkinter import *

#def save():
#	#Code to be written
#	pass

#def load():
#	#Code to be written
#	pass

#master = Tk()
#master.geometry("300x300")

#frame = Frame(master)
#frame.pack()

#mainmenu = Menu(frame)

#mainmenu.add_command(label = "Save", command = save)
#mainmenu.add_command(label = "Load", command = load)
#mainmenu.add_command(label = "Exit", command = master.destroy)

#master.config(menu = mainmenu)
#master.mainloop()









#####################################################################
####################=##=########################=###########





# Tkinter Menu Example 2.

# In this example, we use a hierarchical approach. This approach allows for drop down menu’s within your menu. 
# Think of it as Nested Menu, where we have one main menu, which further contains 2 or more menus. We use the add_cascade to achieve this.

# To keep the code size small and since this is only a demonstration, all commands lead back to an empty
# procedure. Furthermore, you should keep the value of tearoff equal to 0. This prevents the menu from
# being “torn off” into a new window. Most of you will not want this to show as it doesn’t look good visually.

# Note the trend of values that the parameter master has taken. The main menu links to root, while the three
# Sub Menu’s link back to the Main menu.





from tkinter import *



def empty_func() :
	# any code 
	pass

		
def open_func() :
	print("Open")

	
def save_func() :
	print("Save")

	
def exit_func() :
	print("Exit")
	master.destroy()
	

def find_func() :
	print("Find")

	
def debugger_func() :
	print("Debugger")

	
def replace_func() :
	print("Replace")


def documentation_func() :
	print("Documentations")
	
	
master = Tk()

# main menu
main_menu = Menu(master)

# menu 1
file_menu = Menu( master , tearoff = 0 )
file_menu.add_command( label = "Open" , command = open_func )									
file_menu.add_command( label = "Save" , command = save_func )
file_menu.add_separator()
file_menu.add_command( label = "Exit" , command = exit_func )

main_menu.add_cascade( label = "File" , menu = file_menu )


# menu 2
tool_menu = Menu( master , tearoff = 0 )
tool_menu.add_command( label = "Find" , command = find_func)									
tool_menu.add_command( label = "Debugger" , command = debugger_func)
tool_menu.add_command( label = "Replace" , command = replace_func)

main_menu.add_cascade( label = "Tools" , menu = tool_menu )


# menu 3
help_menu = Menu( master , tearoff = 0 )
help_menu.add_command( label = "Documentations" , command = documentation_func)									

main_menu.add_cascade( label = "Help" , menu = help_menu )


master.config(menu = main_menu)

master.mainloop()














