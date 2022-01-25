from tkinter import Tk , ttk , Frame , Button



master = Tk()
master.geometry("300x300")

frame = Frame(master)
frame.pack(padx = 10 , pady = 10 )


var_list = ["Option 1" , "Option 2" , "Option 3" , "Option 4"]				


def retrieve() :
	print(combo.get())

combo = ttk.Combobox( frame , values = var_list )							
combo.set("Pick an option!")
combo.pack(padx = 10 , pady = 10)


button = Button(frame , text = "Submit" , command = retrieve )
button.pack( padx = 10 , pady = 10 )




master.mainloop()

