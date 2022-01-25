from tkinter import Tk , Frame , Scale , HORIZONTAL


master = Tk()
master.geometry("300x300")

frame = Frame(master)
frame.pack()


def v_val(v_value) :
	print(v_value)
	print(type(v_value))


def h_val(h_value) :
	print(h_value)
	print(type(h_value))


# orient in "VERTICAL" by default
v_scale = Scale( frame , from_ = 0 , to = 10 , width = 200 , command = v_val , length = 1000) 												
v_scale.pack( pady = 10 , padx = 10 )

h_scale = Scale( frame , from_ = 0 , to = 10 , orient = HORIZONTAL )
h_scale.config( resolution = 0.5 , command = h_val , length = 2000)
h_scale.config( tickinterval =  1 , sliderlength = 15 )
h_scale.pack( pady = 10 , padx = 10  )























master.mainloop()