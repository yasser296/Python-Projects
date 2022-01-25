
#from tkinter import Tk , Frame , Button , Label , PhotoImage


#master = Tk()
#master.geometry("300x300")

#frame = Frame(master)
#frame.pack()


#image_file = PhotoImage( file = "I-V_characteristic_dpi=400.png" )
#print(image_file)

#"""
#If the image you want to display is not in 
#the same folder/directory, then you’ll 
#have to specify the entire 
#filepath, not just the name of the file.

#"""


#label = Label(master , image = image_file )
#label.pack()


#"""

#Keep in mind that Tkinter itself does not have 
#the ability to control (resize) the images it displays. 
#The image
#displayed above was displayed in it’s original 
#dimensions (size).


#"""











#master.mainloop()




######################################################################################################
######################################################################################################
######################################################################################################


# Displaying Images on a Canvas



#from tkinter import *
#master = Tk() 

#image = PhotoImage(file = "I-V_characteristic_dpi=400.png") 

#canvas = Canvas(width = 300, height = 300, bg='black')

#canvas.create_image(500, 200, image = image)
#canvas.pack()


#master.mainloop()







######################################################################################################
######################################################################################################
######################################################################################################






# Displaying Images on Buttons



"""
In the below code we use a combination of 
PhotoImage + Pillow (python image library) to 
display the image in the required format.

We open the Image using Pillow’s open() function, 
followed by the resize function, which takes a tuple
 
containing the new width and height. 
Then we converted this image to a Tkinter 
compatible format using 
ImageTk.PhotoImage().

"""




from tkinter import *

from PIL import Image , ImageTk




master = Tk()
master.geometry('200x200')

image = Image.open('I-V_characteristic_dpi=400.png')
image_resize_1 = image.resize((200, 200))
image_file_1 = ImageTk.PhotoImage(image_resize_1)

button = Button(width = 200, height = 200, image = image_file_1)

button.pack(padx = 20, pady = 50)

image_resize_2 = image.resize((500, 500))
image_file_2 = ImageTk.PhotoImage(image_resize_2)

label = Label(master , image = image_file_2 )
label.pack()


master.mainloop()

