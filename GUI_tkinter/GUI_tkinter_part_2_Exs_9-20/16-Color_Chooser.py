from tkinter import Tk , Frame , colorchooser , Button , Label , BOTTOM


master = Tk()
master.geometry("300x300")

frame = Frame(master)
frame.pack()


destroy_bttn = Button(master , text = "Destroy Settings window" , command = master.destroy) 			 
destroy_bttn.pack(pady = 10 , padx =10 , side = BOTTOM )



#ask_color = colorchooser.askcolor(title = "Tkinter Color Chooser")

#print(ask_color)
#print(ask_color[0])  # RGB code color 
#print(ask_color[1])  # hexadecimal code color 
#                     # We’ll be needing the hexadecimal code for tkinter


def callback() :
	ask_color = colorchooser.askcolor(title = "Tkinter Color Chooser")
	hex_color = ask_color[1]
	label.config( fg = hex_color)
	print(hex_color)
	
	
	


color_bttn = Button( frame , text = "Choose color" , command = callback)
color_bttn.pack(padx = 10 , pady = 10 )

label = Label(master , text = "Color" , fg = "green" )
label.pack()















master.mainloop()