from tkinter import Tk , Entry , Button , END




master = Tk()
master.geometry("300x300")


def delete_all() :
	input_entry.delete(0 , "end")


def back_space() :
	a = input_entry.get()
	print(a)
	length = len(a)
	print(length)
	input_entry.delete( length-1 , END )

	

input_entry = Entry(master, width = 20 )
input_entry.pack(pady = 10)

delete_all_button = Button(master, text = "Delete all", command = delete_all )
delete_all_button.pack(pady = 10 )

back_space_button = Button(master, text = "Back space", command = back_space )
back_space_button.pack(pady = 10 )

  



master.call( "tk" , "scaling" , 5.0)



master.mainloop()