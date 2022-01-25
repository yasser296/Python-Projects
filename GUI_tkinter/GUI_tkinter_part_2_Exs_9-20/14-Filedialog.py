# Returning a File Path


"""
from tkinter import filedialog 

path = filedialog.askopenfilename(initialdir="/", title="Select file" , filetypes=(("txt files", "*.txt"),("all files", "*.*")))

print( path )
"""

"""
Remember, you can only select files with this, not folders.

Use the askopenfilenames function if you want to select multiple files.

"""






######################################################################################################
######################################################################################################
######################################################################################################




"""
Selecting a File


The difference between the askopenfile function and askopenfilename(s) is that one returns the actual File
object, and one simply returns the file path. In the example below, this is apparent. Where we select a random
text file and see it’s output on screen after calling the read function.


"""

"""
from tkinter import Tk , filedialog 

master = Tk()

path = filedialog.askopenfile(initialdir="/", title="Select file" , filetypes=(("txt files", "*.txt"),("all files", "*.*")))
			

print(path)
print(path.read())


master.mainloop()
"""


"""
The look of the GUI is the exact same as the one for the askopenfilename function. And just like it,
askopenfiles can be used to open several files.

"""






######################################################################################################
######################################################################################################
######################################################################################################





"""
Saving a File


The asksaveasfile function is used to save a file in a specified location. You get to select this location
through the same selection GUI shown in the examples above.

"""



"""

from tkinter import Tk , filedialog 

master = Tk()

path = filedialog.asksaveasfile(initialdir="/", title="Save file" , filetypes=(("txt files", "*.txt"),("all files", "*.*")))
		

print(path)


master.mainloop()
"""

"""
For instance, you may navigate to the Desktop and save a file there with the name of your choice. Be sure to mention the extension when saving the files, otherwise use the defaultextension option to assign an
extension to your files.


The above image shows the GUI for the asksaveasfile function. The biggest difference is the Save button
instead of the Open button.


"""











######################################################################################################
######################################################################################################
######################################################################################################




"""
Selecting a Directory

This function is just like the askopenfilename function, except that it’s not used to select files, rather it
selects directories (folders) and return their file path.
"""



from tkinter import Tk , filedialog 

master = Tk()

path = filedialog.askdirectory(initialdir="/", title="Select file" )
		

print(path)


master.mainloop()


# Be sure not to include the filetypes option here. Folders don’t have filetypes after all