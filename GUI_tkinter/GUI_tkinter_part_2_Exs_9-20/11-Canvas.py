"""
Canvas with arcs

One of the most popular functions, create_arc() is used to draw arcs on the Tkinter Canvas. 
It takes a set of coordinates in the following format X0, Y0, X1, Y1.

"""

#from tkinter import Tk , Frame , BOTH , Canvas




#master = Tk()
#master.geometry("300x300")

#frame = Frame(master , width = 300 , height = 300)
#frame.pack(expand = True , fill = BOTH )

#canvas = Canvas(frame , bg = "white" , width = 300 , height = 300)			



#coordinates = 30 , 60 , 210 , 230
#print(coordinates)
#print(type(coordinates))  # you can make the "coordinates" as a list

#arc = canvas.create_arc( coordinates , start = 0 , extent = 250 , fill = "blue" )
#arc = canvas.create_arc( coordinates , start = 250 , extent = 50 , fill = "red" )
#arc = canvas.create_arc( coordinates , start = 300 , extent = 60 , fill = "yellow" )

#canvas.pack( expand = True , fill = BOTH )



#master.mainloop()

"""
Since all the arcs have the same origin, we give them the same co-ordinates. 
Another thing to note is that the arc extends counter clockwise.

"""




######################################################################################################
######################################################################################################
######################################################################################################



"""
Canvas with Lines

The create_line() function is pretty simple. It takes a set of coordinates for 
two points in the format X0, Y0, X1, Y1 and draws a line between them.


"""

#from tkinter import Tk , Frame , BOTH , Canvas



#master = Tk()

#frame = Frame(master , width = 300 , height = 300)
#frame.pack(expand = True , fill = BOTH )

#canvas = Canvas(frame , bg = "white" , width = 300 , height = 300)			

#coordinates = 50 , 50 , 250 , 250 
#lline = canvas.create_line( coordinates , fill = "blue")

#coordinates = 250 , 50 , 50 , 250 
#lline = canvas.create_line( coordinates , fill = "green")


#canvas.pack( expand = True , fill = BOTH )


#master.mainloop()






######################################################################################################
######################################################################################################
######################################################################################################

"""
Canvas with Image


Using the PhotoImage class you can import photos and turn 
them into a format compatible with other libraries such as Tkinter.


The syntax is pretty simply, you simply pass the 
filepath to the option “file”. You can then pass this file object
into the canvas.create_image() function’s image option.


The two numbers you see, 150 and 150 represent the X and Y location of the origin of the image. 
Since we set the origin to the center of the canvas, the image shows up in the center.



"""


#from tkinter import Tk , Frame , BOTH , Canvas , PhotoImage



#master = Tk()

#frame = Frame(master , width = 300 , height = 300)
#frame.pack(expand = True , fill = BOTH )

#canvas = Canvas(frame , bg = "white" , width = 300 , height = 300)			

#image_file = PhotoImage(file = "I-V_characteristic_dpi=400.png" )

#canvas_image = canvas.create_image( 150 , 150 , image = image_file )


#canvas.pack( expand = True , fill = BOTH )


#master.mainloop()







######################################################################################################
######################################################################################################
######################################################################################################



"""
Canvas with Scrollbar


You can also use Canvas with another Tkinter widget 
called Scrollbar. To learn more about scrolling in

Canvases, follow the link to the Scrollbar widget.

"""


from tkinter import Tk , Frame , BOTH , Canvas , Scrollbar , HORIZONTAL , VERTICAL , BOTTOM , RIGHT , LEFT , X , Y



master = Tk()

frame = Frame(master , width = 300 , height = 300)
frame.pack(expand = True , fill = BOTH )

canvas = Canvas(frame , bg = "white" , width = 300 , height = 300 , scrollregion = ( 0 , 0 , 600 , 600 ) )			

h_bar = Scrollbar( frame , orient = HORIZONTAL , command = canvas.xview )
h_bar.pack( side = BOTTOM , fill = X )
#h_bar.config( command = canvas.xview )

v_bar = Scrollbar( frame , orient = VERTICAL , command = canvas.yview )
v_bar.pack( side = RIGHT , fill = Y )
#v_bar.config( command = canvas.yview )


canvas.config( xscrollcommand = h_bar.set , yscrollcommand = v_bar.set )
canvas.pack( expand = True , side = LEFT , fill = BOTH )


master.mainloop()


















